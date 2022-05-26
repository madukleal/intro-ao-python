# Você é a professora de Ciências e está lançando as notas das alunas.
# Você quer criar um sistema no qual suas alunas podem ver suas notas digitando o nome.
# As listas de alunas e notas se encontra abaixo. As notas podem variar de 0 a 100.
# Nessas listas, as notas estão na mesma ordem dos nomes, ou seja, a aluna no índice 4 tirou a nota no índice 4.

import colorama
from colorama import Fore

alunas = ['Adriana', 'Bárbara', 'Franciele', 'Laís', 'Maria', 'Nayara', 'Patrícia', 'Renata', 'Sarah', 'Thainá']
notas = [78, 57, 80, 98, 54, 89, 90, 100, 71, 85]

# Comece o programa perguntando o nome da aluna.

user_name = input('Qual o seu nome?: ')
# Procure o nome digitado na lista de nomes e imprima uma mensagem com a nota que ela tirou.
if user_name in alunas:
    indice_aluna = alunas.index(user_name)
    if notas[indice_aluna] > 90:
        # Notas a partir de 90 devem ser impressas com a cor verde.
        print( f'{user_name}, sua nota é: ', Fore.GREEN + str(notas[indice_aluna]))
    else:
        # notas abaixo de 60 devem ser impressas com a cor vermelha
        print(f'{user_name}, sua nota é:', Fore.RED + str(notas[indice_aluna]))
# Se o nome digitado não existir na lista, imprima uma mensagem de erro usando a cor vermelha.
else:
    print(Fore.RED + 'A aluna procurada não está matriculada nessa turma')
