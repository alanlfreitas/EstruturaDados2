from os import system as sys


def notas_aluno():
    notas           =   []  #Armazenar notas
    contador        =   1   #Definir inicio do contador
    situacao        =   []
    while contador  <   5:  #loop para informar notas
        sys("clear")  #limpar cmd
        notas.append(float(input(f'Informe a {contador} a nota: ')))    #informação pedida para usuario
        contador    +=  1   #incrementar contagem
        maior_nota  =   max(notas)  #Armazenar maior nota
        menor_nota  =   min(notas)  #Armazenar menor nota
        media       =   sum(notas)/len(notas)   #Calcular e armazenar media
        
#-------------------Verificar situação-------------------------

    if media >= 8:
        situacao = 'Situação: Aprovado'
    elif media > 4 and media < 8:
        situacao = 'NEF, repense sua vida.'
    else:
        situacao = 'Reprovado'
        
#-------------------Imprimir boletim----------------------------       
 
    sys("clear")  #limpar cmd

        
    print(f'''
        ===============================

        Menor nota:  {menor_nota}       
        Maior nota:  {maior_nota}
        Media final: {media}
       
        Situação:    {situacao}
        
        ===============================
        ''')

#--------------------MAIN--------------------------------------------

notas_aluno()



#Aula com Ververton
#Inserindo elemento em uma posição FILE
minha_lista = [1,2,3]
minha_lista.insert(0,6)
print(minha_lista)
#anexar um item ano final da lista
lista=[1,2,3,4]
lista.append(7)
print(lista)
#ordenar lista
lista1=[1,9,4,6]
lista1.sort()
print(lista1)
#ordenar de forma decrescente item da lista
lista1.reverse()
print(lista1)
#remover item da lista
lista1.remove(9)
print(lista1)
#encontrar indice de um item pesquisado
lista2=[1,2,2,2,3,4,5]
print(lista2.index(3))
#encontrar o valor minimo na lista
print(min(lista2))
#encontrar o valor maximo na lista
print(max(lista2))
#contar elementos redundantes da lista em uma lista
print(lista2.count(2))
#concatenar elementoda lista 
lista3=[1,2,2,2,3,4,5]
print(lista2+lista3)
#concatenar lista
lista4 = lista2+lista3
print(lista4)
#verificar a existencia de itens na lista
lista_compra=['banana','maça','laranja']
print('pera' in lista_compra)
#outros metodos de lista
numeros=[1,3,5,7]
print(min(numeros))
print(max(numeros))
#soma os valores da lista
print(sum(numeros))
#################### Criação de listas ####################

minha_lista = [1,2,3,4]
print(minha_lista)

lista = ['banana', 'uva', 'maçã', 'pera']
print(lista[0]) #displays the item in a specific position
print(len(lista[1])) #LEN determines the size of the list or the size of an intem in a list
print(lista[-3]) # negative numbers prints the intem in the position counting backwards
print(lista[:-1])
print(lista[1:])
print(lista[0:2])
print(lista[-1::-1]) # -1::-1 prints the list backwards


#exemplo de notas com listas
notas=[]
contador=1
while contador <5:
  notas.append(float(input(f'Informe a {contador} nota: ')))
  contador+=1
  maior_nota = max(notas)
  menor_nota = min(notas)
  media = sum(notas) / len(notas)
print(f'''
    
    ********************************
       A sua menor nota é: {menor_nota}.
       A sua maior nota é: {maior_nota}.
       A media final é: {media}.
    ********************************
    
    ''')