from sqlalchemy import create_engine, text

#Variaveis de conexão
host = 'localhost'
user = 'root'
password = ''
database = 'exemplo_vendas_aula1'

#Url de conexão
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

query = 'SELECT * FROM vendas'

#Estabelecendo a conexão:
with engine.connect() as conexao:
    resultados = conexao.execute(text(query))

#print (resultados)
for item in resultados:
    print(f'Produto: {item[0]}, Data Venda: {item[1]}, Categoria: {item[2]}, Loja: {item[3]}, Valor: {item[4]}, Quantidade: {item[5]}')