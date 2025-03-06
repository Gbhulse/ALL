#TABUADA

while True:
    c = 1
    n = int(input('Digite um número que direi a tabuada dele: \n'))
    if n < 0:
        break
    while c < 11:
        print(f'{n*c} = {n}*{c} ')
        c += 1
    
    

