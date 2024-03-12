'''
As funções permitem modularizar o código, dividir ele em partes
menores que podem ser reaproveitadas. Isso simplifica a codificação.

Estrutura função em python

def_nomefuncao(param1, param2,3):
   //algum código que a função faz 
   return saída_da_funcao


#cria uma função que calcula a área do triângulo
def calculateTriangleArea(base, altura):
    area = (base * altura) / 2
    return area:

#Exemplo 1: chamar a função
area1 = calculateTriangleArea(100, 10)
print("A área do triângulo é: ", area)

#Exemplo 2: chamar a função novamente
base = float("Digite a base: ")
altura = float("Digite a altura: ")
area2 = calculateTriangleArea(base, altura)
print("A área do triângulo 2 é: ", area2)
'''