num = int(input('Digite um número inteiro: '))
c = int(input('Você quer transformar esse número em Hexadecimal[DIGITE 1] em Octal[Digite 2] ou wm binário[digite 3]? '))

if c == 1:
    print(f'O número em Hexadecimal é: {hex(num)} ')
elif c == 2:
    print(f'O número em Octal é {oct(num)} ')
elif c == 3:
    print(f'O número em Binário é {bin(num)} ')
else:
    print('Favor digitar entre 1 a 3')
    