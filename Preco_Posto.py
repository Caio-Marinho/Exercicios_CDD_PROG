"""Escreva um algoritmo que leia o número de litros vendidos e o tipo de combustível
(codificado da seguinte forma: E-etanol, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente,
sabendo-se que o preço do litro da gasolina é R$ 5,80 e o preço do litro do etanol é R$ 4,90."""
litro = float(input("Informe quantos litros foi colocado em seu veiculo: "))
combustivel = input("Informe qual tipo de combustivel foi colocado. \n"
                    "Digite...\n(E) para Etanol e (G) para Gasolina: ")

if (combustivel != "E" and combustivel != "e") and (combustivel != "G" and combustivel != "g"):
    print("Esse tipo de combustivel não existe!!")
    if combustivel == "E" or combustivel == "e":
        tipoCombustivel = 'Etanol'
        valorCombustivel = 4.90
        valorTotal = litro * valorCombustivel
        print(f"O combustivel escolhido foi o {tipoCombustivel} tendo colocado {litro} Litro(s) totalizando "
              f"um valor total de R$ {valorTotal:.2f}")
    else:
        tipoCombustivel = 'Gasolina'
        valorCombustivel = 5.80
        valorTotal = litro * valorCombustivel
        print(f"O combustivel escolhido foi o {tipoCombustivel} tendo colocado {litro} Litro(s) totalizando "
              f"um valor total de R$ {valorTotal:.2f}")
