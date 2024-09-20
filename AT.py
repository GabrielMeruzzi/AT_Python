import pandas as pd
from pandas.core.frame import DataFrame
import sqlalchemy as sqla
import re
import urllib.request
from bs4 import BeautifulSoup

def exercicio_1():
  acessos = ['192.168.0.1', '192.168.0.2', '192.168.0.3', '192.168.0.4', '192.168.0.1', '192.168.0.3', '192.168.0.4', '192.168.0.5', '192.168.0.6', '192.168.0.1', '192.168.0.6']
  histograma = {}

  try:
    for ip in acessos:
      if ip not in histograma:
        histograma[ip] = 1
      else:
        histograma[ip] += 1
    print(histograma)
  except Exception as e:
    print(e)
  
def exercicio_2():
  sinonimos = {
    'belo': 'bonito', 'casa': 'lar', 'longe': 'distante', 'apos': 'depois'
  }

  try:
    def isSinonimo(dic, palavra1, palavra2):
      for key, value in dic.items():
        if (key == palavra1 and value == palavra2) or (key == palavra2 and value == palavra1):
          return True
        else:
          return False
  except KeyError as e:
    print(e)
  except Exception as e:
    print(e)

  print(isSinonimo(sinonimos, 'belo', 'bonito'))

def exercicio_3():
  conjunto = {'a','o','p','h','t','y','n','l','k','m'}

  try:
    def verPalavraConj(conj, palavra):
      palavraSplit = list(palavra)
      resultado = ''
      for i in palavraSplit:
        for y in conj:
          if i == y:
            resultado += i

      if resultado == palavra:
        return True
      else:
        return False
  except TypeError as e:
    print(e)
  except Exception as e:
    print(e)
    
  print(verPalavraConj(conjunto, 'python'))

def exercicio_4():
  prod1 = ('Sabonete', 10.99, 5)
  prod2 = ('Shampoo', 11.29, 7)
  prod3 = ('Condicionador', 4.99, 10)

  lista = [prod1, prod2, prod3]

  print(lista)

def exercicio_5():
  def adicionar_produtos_via_json(estoque, arquivo_json):
      try:
        df = pd.read_json(arquivo_json)
      except ValueError:
        print("Não foi possivel ler o arquivo JSON. Verifique o JSON.")
      except Exception as e:
        print(f"Erro ao carregar o arquivo JSON: {e}")

      try:
        estoqueDf = pd.DataFrame(estoque)
        df = pd.concat([df, estoqueDf], ignore_index=True)
        print(df)
        df.to_json(arquivo_json, orient='records')
      except Exception as e:
        print(f"Erro ao adicionar produto ao JSON: {e}")

  produto = [{'nome': 'Mousepad', 'preco': 11.99, 'quantidade': 10}]
  json = 'ex_5/estoque.json'
  
  adicionar_produtos_via_json(produto, json)

def exercicio_6():
  def calcular_valor_total_estoque(estoque):
    total = 0

    try:
      for row in estoque:
        total += row[1] * row[2]
    except IndexError:
      print("O JSON está faltando informações.")
    except ValueError:
      print("Verifique se o valor de preço e quantidade estão corretos.")
    except TypeError:
      print("Verifique se o tipo de preço e quantidade estão corretos.")

    print(f"Total: {total}")
    return total

  try:
    df = pd.read_json('ex_5/estoque.json')
  except ValueError:
      print("Não foi possivel ler o arquivo JSON. Verifique o JSON.")
  except Exception as e:
      print(f"Erro ao carregar o arquivo JSON: {e}")
    
  listDf = df.values.tolist()
  calcular_valor_total_estoque(listDf)

def exercicio_7():
  def vender_produto(estoque, nome, qnt_vendida):
    try:
      for row in estoque:
        if row[0] == nome:
          print(row)
          if qnt_vendida > row[2]:
            raise Exception("A quantidade vendida foi maior que o estoque")
          else:
            row[2] -= qnt_vendida
            print(row)
    except IndexError:
      print("O JSON está faltando informações.")
    except ValueError:
      print("Verifique se o valor de preço e quantidade estão corretos.")
    except TypeError:
      print("Verifique se o tipo de preço e quantidade estão corretos.")
      
  try:
    df = pd.read_json('ex_5/estoque.json')
  except ValueError:
      print("Não foi possivel ler o arquivo JSON. Verifique o JSON.")
  except Exception as e:
      print(f"Erro ao carregar o arquivo JSON: {e}")

  listDf = df.values.tolist()
  vender_produto(listDf, 'Mouse Gamer', 17)

def exercicio_8():
  def salvar_csv(estoque):
    print(estoque)

    try:
      estoque.to_csv('ex_8/estoque.csv', index=False)
    except FileNotFoundError:
      print("Diretorio nao existe.")
    except Exception as e:
      print(f"Ocorreu um erro: {e}")
    
  try:
    df = pd.read_json('ex_5/estoque.json')
    salvar_csv(df)
  except ValueError:
    print("Não foi possivel ler o arquivo JSON. Verifique o JSON.")
  except Exception as e:
    print(f"Erro ao carregar o arquivo JSON: {e}")

def exercicio_9():
  funcionarios = {
    'id': [1, 2, 3, 4, 5],
    'nome': ['Joao', 'Gabriel', 'Thiago', 'Felipe', 'Neymar'],
    'departamento': ['TI', 'RH', 'TI', 'Gerencia', 'Jogador']
  }

  avaliacoes = {
    'id': [1, 2, 3, 4],
    'Avaliacao': ['Muito bom', 'Bom', 'Excelente', 'Razoavel']
  }

  df_criando_funcionarios = pd.DataFrame(funcionarios)
  df_criando_avaliacoes = pd.DataFrame(avaliacoes)

  try:
    with pd.ExcelWriter('ex_9/funcionarios.xlsx') as writer:
      df_criando_funcionarios.to_excel(writer, sheet_name='funcionarios', index=False)
    
    with pd.ExcelWriter('ex_9/avaliacoes.xlsx') as writer:
      df_criando_avaliacoes.to_excel(writer, sheet_name='avaliacoes', index=False)
  except ValueError as e:
    print(f"Valor incorreto: {e}")
  except FileNotFoundError:
    print("Diretorio nao existe.")
  except Exception as e:
    print(f"Ocorreu um erro: {e}")

  try:
    df_funcionarios = pd.read_excel('ex_9/funcionarios.xlsx')
    df_avaliacoes = pd.read_excel('ex_9/avaliacoes.xlsx')
  except FileNotFoundError:
    print("Diretorio nao existe.")
  except Exception as e:
    print(f"Ocorreu um erro: {e}")

  try:
    excels_merged = pd.merge(df_funcionarios, df_avaliacoes, on='id')
    excels_merged.to_excel('ex_9/merged.xlsx', sheet_name='Funcionarios avaliados', index=False)
    df_merged = pd.read_excel('ex_9/merged.xlsx')
  except ValueError as e:
    print(f"Erro no valor: {e}")
  except Exception as e:
    print(e)
    
  print(df_merged)

def exercicio_10():
  medicoes = {
      'data_medicao': [
          '2024-09-01 08:00', 
          '2024-09-01 09:00', 
          '2024-09-01 19:00', 
          '2024-09-01 11:00', 
          '2024-09-01 20:00'
      ],
      'temperatura': [36.5, 23.0, 21.8, 24.1, 25.3],
      'umidade': [25, 60, 58, 57, 62],
      'nivel_uv': [3.5, 4.0, 3.8, 4.2, 2.5],
      'luminosidade': [1200, 1300, 800, 1400, 2000],
      'ml_chuva': [0.5, 0.0, 0.0, 0.5, 0.2]
  }

  df_medicoes = pd.DataFrame(medicoes)

  try:
    with pd.ExcelWriter('ex_10/medicoes.xlsx') as writer:
      df_medicoes.to_excel(writer, sheet_name='medicoes', index=False)
  except ValueError as e:
    print(f"Valor incorreto: {e}")
  except FileNotFoundError:
    print("Diretorio nao existe.")
  except Exception as e:
    print(f"Ocorreu um erro: {e}")

  df = pd.read_excel('ex_10/medicoes.xlsx')
  df['data_medicao'] = pd.to_datetime(df['data_medicao'])
  
  verificacoes = {
    'revisao': [],
    'motivo': []
  }

  try:
    for index, row in df.iterrows():
      if row['umidade'] < 30 and row['temperatura'] > 35 and row['ml_chuva'] > 0:
          verificacoes['revisao'].append(row.to_dict())
          verificacoes['motivo'].append('Umidade baixa para alta temperatura e chuva.')

      if row['nivel_uv'] > 3 and (row['data_medicao'].hour < 8 or row['data_medicao'].hour > 17):
          verificacoes['revisao'].append(row.to_dict())
          verificacoes['motivo'].append('Nível UV elevado fora do horário de pico.')

      if row['luminosidade'] > 1000 and (row['data_medicao'].hour > 18 or row['data_medicao'].hour < 6):
          verificacoes['revisao'].append(row.to_dict())
          verificacoes['motivo'].append('Luminosidade elevada fora do horário diurno.')
  except KeyError as e:
    print(f"Index incorreto: {e}")
  except TypeError as e:
    print(f"Tipo incorreto: {e}")
  except Exception as e:
    print(f"Erro: {e}")

  
  try:
    df_medicoes_verf = pd.DataFrame(verificacoes)
    with pd.ExcelWriter('ex_10/medicoes_verificadas.xlsx') as writer:
      df_medicoes_verf.to_excel(writer, sheet_name='medicoes', index=False)
  except ValueError as e:
    print(f"Valor incorreto: {e}")
  except FileNotFoundError:
    print("Diretorio nao existe.")
  except Exception as e:
    print(f"Ocorreu um erro: {e}")
  
  df_verf = pd.read_excel('ex_10/medicoes_verificadas.xlsx')
  print(df_verf)
    
def exercicio_11():
  engine_alunos = sqla.create_engine("sqlite:///ex_11/alunos.sqlite")
  engine_disciplina = sqla.create_engine("sqlite:///ex_11/disciplina.sqlite")

  metadata = sqla.MetaData()

  alunos_table = sqla.Table(
    'aluno', metadata,
    sqla.Column('id', sqla.Integer, primary_key=True),
    sqla.Column('nome', sqla.String),
    sqla.Column('email', sqla.String),
  )
  
  disciplina = sqla.Table(
    'disciplina', metadata,
    sqla.Column('id', sqla.Integer, primary_key=True),
    sqla.Column('nome_disciplina', sqla.String),
    sqla.Column('nota', sqla.Integer),
    sqla.Column('aluno_id', sqla.Integer, sqla.ForeignKey('aluno.id')),
  )

  metadata.create_all(engine_alunos)
  metadata.create_all(engine_disciplina)

def exercicio_12():
  engine_alunos = sqla.create_engine("sqlite:///ex_11/alunos.sqlite")
  engine_disciplina = sqla.create_engine("sqlite:///ex_11/disciplina.sqlite")

  metadata = sqla.MetaData()

  alunos_table = sqla.Table(
    'aluno', metadata,
    sqla.Column('id', sqla.Integer, primary_key=True),
    sqla.Column('nome', sqla.String),
    sqla.Column('email', sqla.String),
  )

  disciplina = sqla.Table(
    'disciplina', metadata,
    sqla.Column('id', sqla.Integer, primary_key=True),
    sqla.Column('nome_disciplina', sqla.String),
    sqla.Column('nota', sqla.Integer),
    sqla.Column('aluno_id', sqla.Integer, sqla.ForeignKey('aluno.id')),
  )

  metadata.create_all(engine_alunos)
  metadata.create_all(engine_disciplina)

  with engine_alunos.connect() as conn:
    conn.execute(sqla.text("drop table aluno"))
  with engine_disciplina.connect() as conn:
    conn.execute(sqla.text("drop table disciplina"))
  exercicio_11()

  with engine_alunos.connect() as conn:
    with conn.begin():
      conn.execute(alunos_table.insert().values(nome="Paulo Torres",email="paulo@gmail.com"))
      conn.execute(alunos_table.insert().values(nome="Gabriel Felipe",email="gabriel@gmail.com"))
      conn.execute(alunos_table.insert().values(nome="Junior Soares",email="junior@gmail.com"))
  
  with engine_disciplina.connect() as conn:
    with conn.begin():
      conn.execute(disciplina.insert().values(nome_disciplina="Python para Dados",nota=5, aluno_id=1))
      conn.execute(disciplina.insert().values(nome_disciplina="SQL",nota=7, aluno_id=1))
      conn.execute(disciplina.insert().values(nome_disciplina="Python para Dados",nota=6, aluno_id=2))
      conn.execute(disciplina.insert().values(nome_disciplina="PB",nota=8, aluno_id=3))
      conn.execute(disciplina.insert().values(nome_disciplina="SQL",nota=5, aluno_id=2))
      conn.execute(disciplina.insert().values(nome_disciplina="PB",nota=5, aluno_id=2))
      conn.execute(disciplina.insert().values(nome_disciplina="SQL",nota=5, aluno_id=3))
      conn.execute(disciplina.insert().values(nome_disciplina="PB",nota=5, aluno_id=1))
      conn.execute(disciplina.insert().values(nome_disciplina="Python para Dados",nota=10, aluno_id=3))

  with engine_disciplina.connect() as conn:
    res = conn.execute(sqla.text("SELECT MAX(nota) FROM disciplina"))
    nota_max = res.fetchone()[0]
    conn.execute(sqla.text(f"UPDATE disciplina SET nota = {nota_max} where nome_disciplina = 'Python para Dados' and aluno_id = 1"))
    conn.commit()
  
  with engine_alunos.connect() as conn:
    res = conn.execute(sqla.text("select * from aluno"))
    print(res.fetchall())
  with engine_disciplina.connect() as conn:
    res = conn.execute(sqla.text("select * from disciplina"))
    print(res.fetchall())

def exercicio_13():
  url = 'https://www.gutenberg.org/browse/scores/top'
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

  request = urllib.request.Request(url, headers=headers)
  response = urllib.request.urlopen(request)
  html = response.read().decode('utf-8')
  soup = BeautifulSoup(html, 'html.parser')
  
  table = soup.find('table')
  th = table.find_all('th')
  td = table.find_all('td')
  downloads = {}
  
  for i in th:
    for y in td:
      downloads[i.text] = y.text

  print(downloads)

def exercicio_14():
  url = 'https://www.gutenberg.org/browse/scores/top'
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

  request = urllib.request.Request(url, headers=headers)
  response = urllib.request.urlopen(request)
  html = response.read().decode('utf-8')
  soup = BeautifulSoup(html, 'html.parser')
  
  ol = soup.find('ol')
  li = ol.find_all('li')
  lista = []
  ordem = 1
  
  for i in li:
    nome = i.text
    nome_filtrado = nome.split('(')[0].strip()
    downloads = nome.split('(')[1].strip('()')
    a = i.find('a')
    link = "https://www.gutenberg.org" + a.get('href')
    lista.append([f"{ordem}. {nome_filtrado} - Downloads: {downloads} Link: {link}"])
    ordem += 1

  print(lista)

def exercicio_15():
  url = 'http://quotes.toscrape.com/'
  
  response = urllib.request.urlopen(url)
  html = response.read().decode('utf-8')
  
  soup = BeautifulSoup(html, 'html.parser')
  
  quotes = soup.find_all('div', class_='quote')
  
  padrao_limpeza = re.compile(r'[^\w\s]')
  
  palavra_chave = "life"
  
  for i in quotes:
    citacao = i.find('span', attrs={'class': 'text'})
    citacao_filter = padrao_limpeza.sub('', citacao.text)
    citacao_split = citacao_filter.split()
    
    for y in citacao_split:
      if y.lower() == palavra_chave:
        print(citacao.text)
        
        autor = i.find('small', attrs={'class': 'author'})
        
        print(f"Autor: {autor.text}")

def exercicio_16():
  print('A Amazon utiliza estrutura dinâmica de dados, ou seja, os dados são carregados através do JavaScript e não estão presentes no HTML, dificultando o WebScraping utilizando o beatiful soup.') 

# NÃO EDITE O CÓDIGO ABAIXO

def main():
  functions = [
      exercicio_13
  ]

  for func in functions:
    print(f"Executando exercício {func.__name__}()")
    try:
      func()
    except Exception as e:
      print(f"Ocorreu um erro ao executar o exercício {func.__name__}()")
      print(e)


if __name__ == "__main__":
  main()
