#programa que le o ano de nascimento de 7 pessoas e quantas sao de maior
#criar uma lista vazia
#adicionar 7 elementos na lista
#percorrer lista e mostrar quantas sao de maior com base em um calculo
#calculo = nascimento - 2026 -> idade
#idade < 18 é de menor, senao é de maior

lista = []
for i in range(7):
    nascimento = int(input(f"Digite o ano de nascimento da pessoa {i+1}: "))
    lista.append(nascimento)

contador = 0
print(lista)
for data in lista:
    idade = 2026 - data
    if idade >= 18:
        print("A pessoa é de maior")
        contador += 1
    else:
        print("A pessoa é de menor")

print(f"Pessoas de maior: {contador}")