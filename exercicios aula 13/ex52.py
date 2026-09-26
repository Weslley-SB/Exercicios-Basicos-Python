# numero primo
# ele é divisivel por 1 e por ele mesmo

numero = int(input("Digite um numero: "))

e_primo = True

if numero <= 1:
    e_primo = False
else:
    for i in range(2, numero):
        if numero % i == 0:
            e_primo=False
            break

print(e_primo)