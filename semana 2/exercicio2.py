'''
Exercício 2:
Crie um programa que lê do teclado a nota
e a quantidade de faltas de um aluno. O
programa deve imprimir reprovado, se:
A nota for menor que 6 ou se as presencas
forem menor do que 75 e aprovado 
caso contrário.
'''

def verificar_aprovacao(nota, faltas):
    if nota < 6 or faltas < 75:
        print("Reprovado")
    else:
        print("Aprovado")

def main():
    nota = float(input("Digite a nota do aluno: "))
    faltas = int(input("Digite a quantidade de faltas do aluno: "))
    
    verificar_aprovacao(nota, faltas)

if __name__ == "__main__":
    main()
