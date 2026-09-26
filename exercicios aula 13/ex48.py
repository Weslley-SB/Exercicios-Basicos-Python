#calcular a soma de todos os numeros impares multiplos de 3 entre 1 e 500

soma = 0
for i in range(1, 501):
    if i % 3 == 0:
        if i % 2 != 0:   
            print(i)
            soma += i

print(f"a soma é de todos os numeros são {soma}")