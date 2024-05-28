import re
import random

def read_file_to_list(filename):
    lines = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                lines.append(line.strip())
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    except IOError:
        print(f"Ошибка при чтении файла {filename}.")
    return lines

def choiseOfLine():
    choise_line = random.choice(lines := read_file_to_list('input.txt'))
    return choise_line

def choiseOfName():
    choise_name = random.choice(read_file_to_list('names.txt'))
    return choise_name

def templateOrigin ():
    line = choiseOfLine()
    words = re.split(r'(#\S+#)', line)
    name = choiseOfName()
    for number in range(len(words)):
        if len(words[number]) > 1:
            if words[number][0] == '#' and words[number][-1] == '#' and len(words[number]) > 2:
                words[number] = name
    print (words, name)

if __name__ == "__main__":
    filename = "input.txt"
    # lines = read_file_to_list(filename)
    # print("Содержимое файла построчно:")
    # for line in lines:
    #     print(line)
    # print(lines)
    templateOrigin()
    
