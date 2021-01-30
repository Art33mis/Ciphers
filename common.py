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


def co_en_aff(d_keys, ch1, key1, key2, alpha_count):
    i_string = input()
    i_string = i_string.lower()
    f_dig = []
    for char in i_string:
        if char.isalpha():
            f_dig.append(d_keys[char])
        else:
            f_dig.append(char)
    for i in range(len(f_dig)):
        if f_dig[i].isdigit():
            if ch1 == "1":
                f_dig[i] = (int(f_dig[i]) * key1 + key2) % alpha_count
            if ch1 == "2":
                f_dig[i] = ((int(f_dig[i]) - key2) * key1) % alpha_count
    f_string = ""
    for i in range(len(f_dig)):
        if str(f_dig[i]).isdigit():
            symbol = list(d_keys.keys())[list(d_keys.values()).index(str(f_dig[i]))]
            f_string = f_string + str(symbol)
        else:
            f_string = f_string + str(f_dig[i])
    return f_string


def get_key1(alpha_count):
    flag = True
    while flag:
        print("Укажите значение первого ключа\n"
              f"Оно не должно быть больше {alpha_count} и не должно делиться на него")
        key1 = int(input())
        if alpha_count % key1 != 0:
            flag = False
    return key1


def get_key2(alpha_count):
    print(f"Введите второй ключ, любое число до {alpha_count}")
    key2 = int(input())
    return key2


def o_keys_file(cipher):
    d_keys = {}
    with open(cipher) as file:
        for line in file:
            key, value = line.split()
            d_keys[key] = value
    return d_keys


def get_r_key(key, alpha_count):
    for i in range(1000):
        if (i * key) % alpha_count == 1:
            r_key1 = i
            break
    return r_key1


def co_en_rec(d_keys, ch1, key1, key2, key3, key4, alpha_count):
    i_string = input()
    i_string = i_string.lower()
    f_dig = []
    for char in i_string:
        if char.isalpha():
            f_dig.append(d_keys[char])
        else:
            f_dig.append(char)
    a_keys = [key1, key2]
    b_keys = [key3, key4]
    for i in range(len(f_dig)):
        if i > 1:
            a_keys.append(a_keys[i - 1] * a_keys[i - 2])
    for i in range(len(f_dig)):
        if i > 1:
            b_keys.append(b_keys[i - 1] + b_keys[i - 2])
    for i in range(len(f_dig)):
        if f_dig[i].isdigit():
            if ch1 == "1":
                f_dig[i] = (int(f_dig[i]) * a_keys[i] + b_keys[i]) % alpha_count
            if ch1 == "2":
                f_dig[i] = ((int(f_dig[i]) - b_keys[i]) * a_keys[i]) % alpha_count
    f_string = ""
    for i in range(len(f_dig)):
        if str(f_dig[i]).isdigit():
            symbol = list(d_keys.keys())[list(d_keys.values()).index(str(f_dig[i]))]
            f_string = f_string + str(symbol)
        else:
            f_string = f_string + str(f_dig[i])
    print(f_string)
