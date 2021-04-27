

def co_or_en():
    flag = True
    while flag:
        print("Выберите действие:\n"
              "1. Зашифровать\n"
              "2. Расшифровать\n"
              "Введите 1, если хотите выбрать первый вариант, и 2, если хотите выбрать 2\n")
        ch1 = input()
        if ch1 == "1" or ch1 == "2":
            flag = False
    return ch1


def co_en_sim(d_keys, ch1):
    if ch1 == "1":
        print("Введите предложение, которое хотите зашифровать")
    if ch1 == "2":
        print("Введите предложение, которое хотите расшифровать")
    i_string = input()
    i_string = i_string.lower()
    c_string = ""
    for char in i_string:
        if char.isalpha():
            if ch1 == "1":
                symbol = d_keys[char]
            if ch1 == "2":
                symbol = list(d_keys.keys())[list(d_keys.values()).index(char)]
            c_string = c_string + str(symbol)
        else:
            c_string = c_string + char
    return c_string


def simple():
    chooser = True
    d_keys = {}
    while chooser:
        print("Введите способ, которым \n"
              "1. Добавить файл с ключом\n"
              "2. Ввести ключ вручную с клавиатуры\n"
              "Введите 1, если хотите выбрать первый вариант, и 2, если хотите выбрать 2\n")
        ch = input()
        if ch == "1" or ch == "2":
            chooser = False
    if ch == "1":
        print("Убедитесь, что файл находится в той же директории, что и проект\n"
              "Введите название файла, включая и его расширение\n")
        o_file = input()
        with open(o_file) as file:
            for line in file:
                key, value = line.split()
                d_keys[key] = value

    if ch == "2":
        e_input = True
        while e_input:
            print("Введите ключ в формате: буква пробел ключ\n"
                  "Пример: a л\n"
                  "Для окончания ввода напечатайте end\n")
            o_string = input()
            if o_string == "end":
                e_input = False
            key, *value = o_string.split()
            d_keys[key] = value
    ch1 = co_or_en()
    c_string = co_en_sim(d_keys, ch1)
    print(c_string)





