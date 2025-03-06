#Bissexto, só me atentar de colocar a igualdade, estava fazendo sem o == 0

ano = int(input('Digite o ano para saber se ele é bissexto: '))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f' O ano {ano} é bissexto')

else:
    print(f' O ano {ano} não é bissexto')

    

