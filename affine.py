

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


def o_keys_file(cipher):
    d_keys = {}
    with open(cipher) as file:
        for line in file:
            key, value = line.split()
            d_keys[key] = value
    return d_keys


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


def get_r_key(key, alpha_count):
    for i in range(1000):
        if (i * key) % alpha_count == 1:
            r_key1 = i
            break
    return r_key1


def co_en_aff(d_keys, ch1, key1, key2, alpha_count):
    i_string = input().lower()
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


def affine():
    print("Укажите количество слов в вашем алфавите")
    alpha_count = int(input())
    d_keys = o_keys_file("lists_of_ciphers/cipher1.txt")
    key1 = get_key1(alpha_count)
    key2 = get_key2(alpha_count)
    ch1 = co_or_en()
    if ch1 == "1":
        print("Введите предложение, которое хотите зашифровать")
        f_string = co_en_aff(d_keys, ch1, key1, key2, alpha_count)
    if ch1 == "2":
        r_key1 = get_r_key(key1, alpha_count)
        print("Введите предложение, которое хотите расшифровать")
        f_string = co_en_aff(d_keys, ch1, r_key1, key2, alpha_count)
    print(f_string)

