# Anotações e códigos de Análise de Dados - UNOPAR

texto = "Aprendendo Python na disciplina de linguagem de programação."

print (f'Tamanho do texto = {len(texto)}') #len é uma função para contar caracteres
print ("Python in texto = {'Python' in texto}") #in é uma função que busca algo e devolve um valor booleano
print ("Quantidade de y no texto = {texto.count('y')}") #count é uma função para contar quantas vezes algo aparece
print(f'As 5 primeiras letras são: {texto[0:6]}') #Percorre texto indo do index 0 até 6, sem incluir o 6 (n-1)
print('\n')

print(texto.upper()) #Transforma todos os char em maiusculo
print(texto.replace("i","XX")) #Função replace troca a primeira posição (i) pela segunda posição (XX),
                              #mas não transofrma a variavel diretamente, apenas quando a salvamos em uma nova varivel"""
print('\n')

palavras = texto.split()
print(f'palavras = {palavras}')
print(f'Tamanho de palavras = {len(palavras)}')
print('\n')

#LISTAS
vogais = ['a', 'e', 'i', 'o', 'u']

for vogal in vogais:
    print(f'Posição = {vogais.index(vogal)}, valor = {vogal}')
print('\n')

vogais2 = []
print(f'Tipo do objeto vogais2 = {type(vogais2)}') #Função Type mostra o tipo

vogais2.append('a')
vogais2.append('e')
vogais2.append('i')
vogais2.append('o')
vogais2.append('u')

for p, x in enumerate(vogais2):
    print(f'Posição = {p}, valor = {x}')
print('\n')

#List Comprehension (ListComp)
linguagens = ['Python', 'Java', 'JavaScript', 'C', 'C#', 'C++', 'Swift', 'Go', 'Kotlin']

#Essa sintaxe resultaria no mesmo fim:
#linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()

print("Antes da listcomp = ", linguagens)
linguagens = [item.lower() for item in linguagens] #Forma Py de se escrever um For
print("\nDepois da listcomp = ", linguagens)

'''o código mostrado seria o mesmo que o seguinte caso fosse feito com for

for i, item in enumerate(linguagens):
    linguagens[i] = item.lower()

print("\nDepois de listcomp = ", linguagens)'''
print('\n')


linguagens_java = [item for item in linguagens if 'java' in item]
print(linguagens_java)

'''seria o mesmo que:
for item in linguagens:
    if 'java' in item:
        linguagens_java.append(item)
'''
print('\n')

#função map() e filter()
linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()

nova_lista = map(lambda x: x.lower(), linguagens)
print(f'A nova lista é = {nova_lista}\n')

nova_lista = list(nova_lista)
print(f'Agora sim, a nova lista é = {nova_lista}')
print('\n')

#filter()
numeros = list(range(0 ,20)) #uma lista contendo todos os numeros de 0-20

numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_pares)
print('\n')

#set()
vogais3 = set('aaeeeioooouuuaaaaaaeeee') #Set cria um conjunto em cada iteravel, eliminando valores duplicados
print(type(vogais3), vogais3)
print('\n')

#Dicionarios (Mapping)
cadastro = {
    'Nome' : ['João', 'Ana', 'Pedro', 'Marcela'],
    'Cidade' : ['São Paulo', 'São Paulo', 'Rio de Janeiro', 'Curitiba'],
    'Idade' : [25, 33 ,37, 18]
}

print('length = ', len(cadastro))

print('Chaves = ', cadastro.keys())
print('Valores = ', cadastro.values())
print('Itens = ', cadastro.items())
print('\n')

quantidade_de_itens = sum([len(cadastro[chave]) for chave in cadastro])

print(f'Quantidade de elementos no dicionário = {quantidade_de_itens}')
print('\n')

import numpy as np #O correto seria no inicio do codigo, mas é apenas para facilitar as anotações nesse caso

matriz_1_1 = np.array([1, 2, 3]) #Cria matriz de 1 linha e 1 coluna
matriz_2_2 = np.array([[1, 2], [3, 4]]) #Cria matriz de 2 linhas e 2 colunas

print(type(matriz_1_1))

print('Matriz 1x1: \n', matriz_1_1)
print('Matriz 2x2: \n', matriz_2_2)

m1 = np.zeros((3,3)) #Cria uma matriz 3x3 com zeros
m2 = np.ones((2,2)) #Cria uma matriz 2x2 com 1s
m3 = np.eye(4) #Cria uma matriz identidade 4x4
m4 = np.random.randint(low=0, high=100, size=10).reshape(2,5) #cria uma matriz 2x5 c num inteiros

print('Zeros 3x3 \n', m1, '\n')
print('1s 2x2 \n', m2, '\n')
print('Identidade 4x4 \n', m3, '\n')
print('Randomica 4x4 \n', m4, '\n')

print(f'Soma dos valores em m4 = {m4.sum()}')
print(f'Valor mínimo em m4 = {m4.min()}')
print(f'Valor máximo em m4 = {m4.max()}')
print('Média dos valores em m4 = ', m4.mean()) #Escrever dessa forma é o mesmo que escrever tudo dentro do ()
                                               # usando format no começo, porém nesse caso não precisa lembrar do f
print('\n')