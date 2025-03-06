from datetime import datetime

ano = int(input('Qual ano você nasceu? '))

n = datetime.now().year 
d = n - ano

if d == 18:
    print(f'\033[1;31m Você deverá se alistar no exercito\033')
elif d>18:
    print(f'\033[1;36m Você já se alistou no exercito e está regular!\033')
else:
    print(f'\033[1;33m Você tem {d} anos, quando tiver 18 deverá se alistar no exercito\033')
