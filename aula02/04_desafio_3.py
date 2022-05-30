
from datetime import datetime, date, time, timedelta

# strftime(format) method -> creates a string representing the time under the control of an explicit format string.
#  datetime.strptime() class method -> creates a datetime object from a string representing a date and time and a corresponding format string.
# datetime.now() -> The date contains year, month, day, hour, minute, second, and microsecond assigned to the now variable
# datetime.now().date() -> datetime.now contains (y/m/d/h/m/s/ms) but with .date() it only shows y/d/m
# date.today() ->  returns a date object, which is assigned to the today variable

# Peça para o usuário digitar a data de seu próximo aniversário no formato brasileiro

user_bday_str = input('qual a data do seu proximo aniversário? (dd/mm/aaaa): ')
user_bday_datetime = datetime.strptime(user_bday_str, '%d/%m/%Y').date()

# Imprima uma mensagem dizendo quantos dias faltam para o aniversário dele

user_bday_countdown = user_bday_datetime - datetime.now().date()
print(f'seu proximo aniversario sera daqui {user_bday_countdown.days} dias')

# Pergunte ao usuário se ele(a) gosta de aniversário e salve a resposta
user_bday = input('voce gosta de fazer aniversario digite sim ou nao:').lower()
# Pergunte ao usuário se ele(a) vai fazer festa e salve a resposta
user_party = input('vc vai fazer festa digite sim ou nao:').lower()
# Imprima uma mensagem dizendo se o usuário vai ganhar presente ou não
# A regra é: o usuário só pode ganhar presente se gostar de aniversário e for fazer festa.
if user_bday and user_party == "sim":
    print('oba vc vai ganhar presentes')
else:
    print('ah q pena, vc n vai ganhar presente')





