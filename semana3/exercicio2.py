'''
Exercício 2 - Semana 3
Crie um programa que imprime usando
for a figura abaixo:
*
**
***
****
*****
******
termina com 10 * na última linha
'''

for i in range(1, 10):
    if i < 11:
        print('*' * i)
    else:
        print('*' * 10)
