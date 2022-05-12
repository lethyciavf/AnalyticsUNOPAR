import pandas as pd

#------------------------------------------------S E R I E S----------------------------------------------------
'''
O que é? Indices com informações, está equiparado a uma lista
Construtor SERIES:
    pandas.Series(data=none, index=none, dtype=none, copy=False, fastpath=False)
    Pode receber varios parametros, para uma serie c dados, data é o unico obrigatorio
    Obs. Quando usar a função, usar S maiúsculo
'''
pd.Series(data = 5) #Usa o construtor para construir uma series de 5 "linhas"

lista_nomes = 'Howard Ian Peter Jonah Kellie'.split()

pd.Series(lista_nomes) #Cria uma serie com uma lista de nomes

dados1 = {
    'nome1' : 'Howard',
    'nome2' : 'Ian',
    'nome3' : 'Peter',
    'nome4' : 'Jonah',
    'nome5' : 'Kellie'
}

pd.Series(dados1) #Cria uma serie a partir de um dict

cpfs = '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split()

pd.Series(lista_nomes, index=cpfs) #Passa a variavel cpfd como index para a serie

print(pd.Series(lista_nomes, index=cpfs))

series_dados1 = pd.Series(lista_nomes, index = cpfs)

print('\n', series_dados1.loc['111.111.111-11']) #localiza a informação contida no index informado, nesse caso o cpf

#Algumas funções para extração de informações em Series
series_dados = pd.Series([10.2,-1,None,15,23.4])

print('\nQuantidade de linhas: ', series_dados.shape) #Retorna uma tupla com o número de linhas
print('Tipos de dados: ', series_dados.dtypes) #Retorna o tipo de dados, se for misto será object
print('Os valores são unicos?', series_dados.is_unique) #Verifica se os valores são únicos
print('Existem valores nulos?', series_dados.hasnans) #Verifica se existem valores nulos
print('Quantos valores existem?', series_dados.count())

print('\nQual o menor valor?', series_dados.min()) #Extrai o menor valor, porém todos od dados precisam ser do mesmo tipo
print('\nQual o maior valor?', series_dados.max()) #Extrai o valor máximo, usa a mesma condição do min
print('\nQual a média aritmética?', series_dados.mean())
print('\nQual desvio padrão?', series_dados.std())
print('\nQual a mediana?', series_dados.median())

print('\nResumo\n', series_dados.describe()) #Exibe um resumo sobre os dados na Serie

#---------------------------------------------D A T A F R A M E S------------------------------------------------
'''
O que é? DataFrames esta equiparado a uma tabela, possui linhas e colunas com dados
Construtor:
    pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
    Assim como em Series, apenas o parametro data é obrigatório na criação
'''

#Iremos reutilizar a var lista_nomes e cpfs, uma vez que o arquivo é o mesmo
lista_emails = 'risus.verius@dictumPhasellusin.ca Nunc@vulputate.ca fames.acturpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@neclutus.co.uk'.split()
lista_idades = [32, 22, 25, 29, 38]

pd.DataFrame(lista_nomes, columns = ['Nome']) #Cria um DataFrame apenas com os nomes, o nome da coluna recebe o título "Nome"

pd.DataFrame(lista_nomes, columns=['Nome'], index=cpfs) #Mesma função da anterior, mas ao invés do index ser default, passa a usar o cpf

dados2 = list(zip(lista_nomes, cpfs, lista_idades, lista_emails)) #Cria uma lista de tuplas

print('\n', pd.DataFrame(dados2, columns=['Nome', 'CPF', 'Idade', 'E-Mail'])) #Cria uma planilha com os dados, como não estou usando Jupyter Notebook que mostra o output, usei a função print para visualizar

#Construindo um DataFrame a partir de um Dict

dados3 = {
    'nomes' : 'Howard Ian Peter Jonah Kellie'.split(), #Não se esquecer da vírgula, Lethycia!
    'cpfs' : '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split(),
    'emails' : 'risus.verius@dictumPhasellusin.ca Nunc@vulputate.ca fames.acturpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@neclutus.co.uk'.split(),
    'idades' : [32, 22, 25, 29, 38]
}

print('\n', pd.DataFrame(dados3))

#Extraindo informações de um DataFrame
df_dados = pd.DataFrame(dados3) #Aloca em uma var o df criado

print('\nInformações do DataFrame:\n')
print(df_dados.info()) #Apresenta informações sobre o DataFrame (DF)

print('\nQuantidade de linhas e colunas: ', df_dados.shape)
print('\nTipo de dados:\n', df_dados.dtypes) #Retorna o tipo de dado para cada coluna, se valores mistos resultara em object

print('\nQual o menor valor de cada coluna?', df_dados.min())
print('\nQual o maior valor?', df_dados.max())
print('\nQual a média aritmética?', df_dados.idades.mean()) #Extrai a média arit das idades (tabela.coluna.função)
print('\nQual desvio padrão?', df_dados.idades.std())
print('\nQual a mediana?', df_dados.idades.median())

print('\nResumo\n', df_dados.describe()) #Exibe um resumo

df_dados.head() #Exibe os 5 primeiros registros do DataFrame

#Criando outros dataframes a partir de colunas de um df
'''
Sintaxes para seleção de colunas em um df:
nome_df.nome_coluna - só pode ser usada para uma coluna
nome_df[nome_coluna] - essa opção funciona para quando for necessário selecionar mais de uma coluna
nome_df[['nome coluna 1', 'nome coluna 2', 'nome coluna 3']] - exemplo de seleção com mais de uma coluna
A seleção de uma coluna resulta em uma "Series"
'''
print('\n')

df_uma_coluna = df_dados['idades']
print(type(df_uma_coluna)) #Resulta em Series

print('Média de idades = ', df_uma_coluna.mean())

print(df_uma_coluna)

print('\n')

colunas = ['nomes', 'cpfs'] #Var com uma lista com as colunas selecionadas
df_duas_colunas = df_dados[colunas] #Passa a lista para a variavel. Python entende que estamos tratando de Pandas devido a variavel já ter sido criada co o tipo de conteudo "df_dados"
#Poderia ter feito direto: df_duas_colunas = df_dados['nomes', 'cpfs']
print(type(df_duas_colunas))
print(df_duas_colunas)