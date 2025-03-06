n = str(input('Diga uma palavra ou frase que direi se é palindromo: \n')).upper().strip()

frase = n.replace(" ", "")

print(f'A frase sem espaço é {frase}')

if frase == frase[::-1]:
    print(f'A frase {frase} é um palindromo')
else:
    print(f'A frase {frase} não é um palindromo ')