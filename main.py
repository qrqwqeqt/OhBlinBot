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

if __name__ == "__main__":
    filename = "input.txt"
    lines = read_file_to_list(filename)
    # print("Содержимое файла построчно:")
    # for line in lines:
    #     print(line)
    print(lines)
    
