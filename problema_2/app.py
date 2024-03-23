import random

def insere_dados(lista):
    while len(lista) < 100:
        lista.append(random.randint(1, 50))

def conta_repeticao(lista, num):
    numero_contagem = 0

    for numero in lista:
        if numero == num:
            numero_contagem += 1

    return numero_contagem

def main():
    lista_dados = []

    insere_dados(lista_dados)

    print(lista_dados)

    numero_usuario = int(input("Insira um número até 50 para procurar na lista de dados: "))

    print(f"O número {numero_usuario} aparece {conta_repeticao(lista_dados, numero_usuario)} vezes na lista de dados!")

if __name__ == "__main__":
    main()