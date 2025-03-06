from datetime import datetime
ano = int(input('Qual ano você nasceu? '))

n = datetime.now().year
d = n - ano

if d < 9:
    print('Você é da categoria MIRIM')
elif 9 <= d < 14: #redundante podia botar <=14 somente
    print('Você é da categoria INFANTIL')
elif 14 <= d < 19: 
    print('Você é da categoria Junior')
elif 19 <= d < 20:
    print('Você é da categoria Senior')
else:
    print('Você é da categoria Master')