'''
Exercício 3 - Semana 3
Crie um programa que lê do teclado
sucessivos números de matricula (int).
O programa deve parar de ler os números 
quando a matricula 0 for digitada.
Ao final deve apresentar os números de 
matriculas separados em 3 grupos.
'''

def separar_grupos(matriculas):
    grupo1 = []
    grupo2 = []
    grupo3 = []
    
    for matricula in matriculas:
        if matricula % 3 == 0:
            grupo1.append(matricula)
        elif matricula % 3 == 1:
            grupo2.append(matricula)
        else:
            grupo3.append(matricula)
    
    return grupo1, grupo2, grupo3

def main():
    matriculas = []
    
    while True:
        matricula = int(input("Digite o número da matrícula (digite 0 para parar): "))
        if matricula == 0:
            break
        matriculas.append(matricula)
    
    grupo1, grupo2, grupo3 = separar_grupos(matriculas)
    
    print("Grupo 1:", grupo1)
    print("Grupo 2:", grupo2)
    print("Grupo 3:", grupo3)

if __name__ == "__main__":
    main()
