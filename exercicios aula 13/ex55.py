#ler 5 pessoas com nome e peso -> dicionario
#ver qual o maior peso e menor peso 

dicionario = {}

for i in range(5):
    pessoa = str(input(f"Pessoa {i+1}: "))
    peso = int(input(f"Peso da pessoa {i+1}: "))
    dicionario[pessoa] = peso

print(dicionario)

def procurar_maior_peso(dicionario): #Usando metodo logico para descobrir maior peso
    pesoz = 0
    for peso in dicionario.values():
        if peso > pesoz:
            pesoz = peso
    resultado = next(filter(lambda x: x[1] == pesoz, dicionario.items()))
    return f"A pessoa {resultado[0]} com peso de {pesoz}kg tem o maior peso"

def procurar_menor_peso(dicionario): #usado função do python para maior flexibilidade
    pesoz = min(dicionario.values())
    resultado = next(filter(lambda x: x[1] == pesoz, dicionario.items()))
    return f"A pessoa {resultado[0]} com peso de {pesoz}kg tem o menor peso"

print(f"{procurar_maior_peso(dicionario)} e {procurar_menor_peso(dicionario)}")