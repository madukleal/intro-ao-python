# Dado um arquivo de entrada, escreva um programa que leia o conteudo do arquivo para uma string,
# e escreva um outro arquivo de saída que imprima o texto ao contrário.
# Exemplo de entrada: Oi mulheres maravilhosas do curso de Python do ConstruDelas!
# Exemplo de saída: !saleDurtsnoC od nohtyP ed\nosruc od sasohlivaram serehlum iO


file = 'entrada_desafio_11.txt'
with open(file, 'r') as file1:
    reading_file1_content = file1.read()
    # print(f'read:{reading_file1_content}')

second_file = 'saida_desafio_11.txt'
with open(second_file, 'w') as file2:
    backwards = reading_file1_content[::-1]

print(backwards)
