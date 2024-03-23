import random

def insere_dados(lista):
    while len(lista) < 100:
        lista.append(random.randint(1, 50))

def conta_repeticoes(lista):
    contagem = {}

    for valor in lista:
        if valor in contagem:
            contagem[valor] += 1
        else:
            contagem[valor] = 1

    return contagem

def main():
    lista_dados = []

    insere_dados(lista_dados)

    contagem = conta_repeticoes(lista_dados)

    for valor, frequencia in contagem.items():
        print(f"O valor {valor} aparece {frequencia} vezes")

    print(lista_dados)    

if __name__ == "__main__":
    main()