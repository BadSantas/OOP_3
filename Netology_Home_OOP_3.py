import os

file_names = ["1.txt", "2.txt", "3.txt"]

file_contents = {}

for file_name in file_names:
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        file_contents[file_name] = lines

sorted_files = sorted(file_contents.items(), key=lambda item: len(item[1]))

with open('result.txt', 'w', encoding='utf-8') as result_file:
    for file_name, lines in sorted_files:
        result_file.write(f"{file_name}\n")
        result_file.write(f"{len(lines)}\n")
        result_file.writelines(lines)
        result_file.write("\n")

print("Объединение файлов завершено. Результат сохранен в 'result.txt'.")