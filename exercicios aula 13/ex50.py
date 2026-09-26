

lista = []
for i in range(6):
    numero = int(input(f"Digite o valor {i+1}: "))
    lista.append(numero)

soma = 0
for numeros in lista:
    if numeros % 2 == 0:
        soma += numeros

print(lista)
print(soma)