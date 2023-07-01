#lista ->  uma sequencia de itens em uma oredm particular 
carros = ["ferrari","lamborgini","fusca" ]

#Interagindo com itens de uma lista 
#print(carros[0])#primeiro item 

#print('Eu "gostaria" de ter uma  ',carros[1])

#print(carros[-1])#ultimo item

#manipulando itens de uma lista 

carrosarros = ["ferrari","lamborgini","fusca" ]

##substituindo elementos

carros[0] = 'mustang'

print(carros)# msutang ,lamborgini,fusca

#acrecentando itens a lista

carros.append('BMW')
print(carros)

#2
carros.insert(1,'jeep')
print(carros)

#separa o item em caracteres
carros.extend('fusca')
print(carros)


#ixcluir itens

#1

del carros[1]
print(carros)

#2 ixclui o ultimo elemento da lista 
carros.pop
print(carros)

#ou

carros.pop(2)
print(carros)

#3

carros.remove('mustang')
print(carros )

#organizando lista 

# em ordem alfabetica

carros.sort()
print(carros)

# em ordem alfabetica inversa
carros.sort(reverse=True)

#ou

print(sorted(carros))
#ou
carros.reverse()
print(carros)

#tamanho da lista
print(len(carros))