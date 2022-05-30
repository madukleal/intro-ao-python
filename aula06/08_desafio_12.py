# Escreva um programa que leia o arquivo "exemplo2.csv", e converta
# os registros desse CSV para o formato JSON. Escreva um arquivo de saída
# que contenha o conteúdo em JSON.
import csv
import json


with open('exemplo2.csv', 'r') as cvs_to_list:
    csv_reader = csv.DictReader(cvs_to_list)
    students_data_list = []
    for student_data in csv_reader:
        students_data_list.append(student_data)


with open('exemplo2.json', 'w') as list_to_jsonfile:
    students_data_json = json.dumps(students_data_list)
    list_to_jsonfile.write(students_data_json)

    print(students_data_json)