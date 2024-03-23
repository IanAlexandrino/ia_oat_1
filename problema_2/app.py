import random

def insere_dados(lista):
    if not lista:
        return 0
    while len(lista) < 100:
        lista.append(random.randint(1,100))

def main():
    lista_dados = []

    insere_dados(lista_dados)

    

if __name__ == "__main__":
    main()