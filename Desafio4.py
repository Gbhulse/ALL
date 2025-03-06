dado = input('Escreva algo: ')
print(f'Esse dado é número? {dado.isdigit()}, é alfanumérico? {dado.isalnum()}, é ASCII? {dado.isascii()}, é decimal? {dado.isdecimal()}, e numérico? {dado.isnumeric()}')
print(f'Esse dado é do tipo {type(dado)}')
