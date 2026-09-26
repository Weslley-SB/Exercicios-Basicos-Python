# frase = "Apos a sopa" -> POLINDROMA

frase = str(input("Digite uma frase para ver se é polindroma: ")).lower()
frase = frase.replace(" ", "")
frase_invertida = frase[::-1]

if frase == frase_invertida:
    print("É polindroma.")
else:
    print("Não é polindroma.")

print(frase_invertida)