

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


def recurrent():
    print("Укажите количество слов в вашем алфавите")
    alpha_count = int(input())
    d_keys = o_keys_file("lists_of_ciphers/cipher1.txt")
    d_keys
    key1 = get_key1(alpha_count)
    key2 = get_key1(alpha_count)
    key3 = get_key2(alpha_count)
    key4 = get_key2(alpha_count)
    ch1 = co_or_en()
    if ch1 == "1":
        print("Введите предложение, которое хотите зашифровать")
        co_en_rec(d_keys, ch1, key1, key2, key3, key4, alpha_count)
    if ch1 == "2":
        r_key1 = get_r_key(key1, alpha_count)
        r_key2 = get_r_key(key2, alpha_count)
        print("Введите предложение, которое хотите расшифровать")
        co_en_rec(d_keys, ch1, r_key1, r_key2, key3, key4, alpha_count)

