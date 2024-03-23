def main():
    lista_meses_temperatura = [
        {"Janeiro": 0, "Fevereiro": 0, "Março": 0, "Abril": 0, "Maio": 0, "Junho": 0, 
         "Julho": 0, "Agosto": 0, "Setembro": 0, "Outubro": 0, "Novembro": 0, "Dezembro": 0}
    ]

    print("Digite a temperatura de ")

    for meses_temperatura in lista_meses_temperatura:
        for mes, temperatura in meses_temperatura.items():
            meses_temperatura[mes] = input(mes + ": ")

    print(lista_meses_temperatura)

if __name__ == "__main__":
    main()