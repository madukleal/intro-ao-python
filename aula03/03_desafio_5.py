# Crie uma lista com 60 números começando com o valor 1 e indo até o número 60 (ou seja, o número 60 deve estar na lista).

sixty_numbers_list = list(range(1, 61))

# minha_lista = list(range(0, 10, 2))
# print("minha_lista: " + str(minha_lista))
# print()

# Imprima todos os itens da sua lista de índice par. Imprima o índice e o item.

print('índice || item')
print('------ | ----')
for i, item in enumerate(sixty_numbers_list):
    if item % 2 == 0:
        print(f'   {i}   |  {item}')

print()
