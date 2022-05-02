
# 1. Pergunte ao usuário em qual cidade e o estado em que ele(a) mora

user_city = input('qual a cidade em que você mora?:').upper()
user_state = input('qual o estado em que você mora?:').lower()

# 2. Imprima uma mensagem diga a cidade em que o usuário mora.
#    O nome da cidade deve estar todo em letras maiúsculas.

print('você mora em ' + user_city + ' :)')

# 3. Imprima uma mensagem diga o estado em que o usuário mora.
#    O nome do estado deve estar todo em letras maiúsculas.
#    Utilize uma forma de formatação de string diferente da que foi usada no item 2.

print(f'você mora no estado do {user_state}')





