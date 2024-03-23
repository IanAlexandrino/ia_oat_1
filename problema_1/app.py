def calcula_media_temperatura(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)

def main():
    lista_temperaturas = []

    lista_meses_temperatura = [
        {"Janeiro": 0, "Fevereiro": 0, "Março": 0, "Abril": 0, "Maio": 0, "Junho": 0, 
         "Julho": 0, "Agosto": 0, "Setembro": 0, "Outubro": 0, "Novembro": 0, "Dezembro": 0}
    ]

    print("Digite a temperatura de ")

    for meses_temperatura in lista_meses_temperatura:
        for mes, temperatura in meses_temperatura.items():
            temperatura_digitada = int(input(f"{mes}: "))
            meses_temperatura[mes] = temperatura_digitada
            lista_temperaturas.append(temperatura_digitada)

    media_temperaturas = calcula_media_temperatura(lista_temperaturas)

    print(lista_meses_temperatura)
    print(lista_temperaturas)
    print(media_temperaturas)

if __name__ == "__main__":
    main()