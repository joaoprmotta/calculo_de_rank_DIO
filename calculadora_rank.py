def calcular_rank(vitorias, derrotas):
    try:
        vitorias = int(vitorias)
        derrotas = int(derrotas)
    except ValueError:
        return "Por favor, insira números válidos."

    saldo = vitorias - derrotas

    if vitorias < 11:
        rank = "Ferro"
    elif vitorias < 20:
        rank = "Bronze"
    elif vitorias < 50:
        rank = "Prata"
    elif vitorias < 80:
        rank = "Ouro"
    elif vitorias < 90:
        rank = "Diamante"
    elif vitorias < 100:
        rank = "Lendário"
    else:
        rank = "Imortal"

    return f"Sua diferença de vitórias e derrotas é {saldo}. Seu rank é {rank}."


def main():
    while True:
        vitorias = input("Quantas vitórias você tem? ")
        derrotas = input("Quantas derrotas você tem? ")

        print(calcular_rank(vitorias, derrotas))

        continuar = input("Quer calcular novamente? (s/n): ")
        if continuar.lower() != "s":
            print("Programa encerrado.")
            break


if __name__ == "__main__":
    main()