def calcular_imc(peso, altura):
    return peso / (altura ** 2)


def classificar_imc(imc, idade, sexo):
    sexo = sexo.lower()

    if idade < 18:
        return (
            "IMC infantil/adolescente.\n"
            "A classificação correta depende de tabelas por idade e sexo."
        )

    elif idade < 60:
        # Adultos (mesma classificação para ambos os sexos)
        if imc < 18.5:
            return "abaixo do popapi"
        elif imc < 25:
            return "Peso pesado"
        elif imc < 30:
            return "Sobrepeso"
        else:
            return "Obesidade a +"

    else:
        # Idosos (faixas levemente diferentes por sexo)
        if sexo == "masculino":
            if imc < 22:
                return "Abaixo do peso (idoso)"
            elif imc <= 27:
                return "Peso adequado (idoso)"
            else:
                return "Sobrepeso (idoso)"

        elif sexo == "feminino":
            if imc < 21:
                return "Abaixo do peso (idosa)"
            elif imc <= 26:
                return "Peso adequado (idosa)"
            else:
                return "Sobrepeso (idosa)"

        else:
            return "Sexo inválido. Use 'masculino' ou 'feminino'."


try:
    peso = float(input("Peso (kg): ").replace(",", "."))
    altura = float(input("Altura (m): ").replace(",", "."))
    idade = int(input("Idade: "))
    sexo = input("Sexo (masculino/feminino): ")

    if peso <= 0 or altura <= 0 or idade <= 0:
        print("Peso, altura e idade devem ser maiores que zero.")
    else:
        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc, idade, sexo)

        print("\nResultado")
        print("-" * 20)
        print(f"IMC: {imc:.2f}")
        print(f"Classificação: {classificacao}")

except ValueError:
    print("Erro: digite valores numéricos válidos.")
