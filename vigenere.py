

def o_keys_file(cipher):
    d_keys = {}
    with open(cipher) as file:
        for line in file:
            key, value = line.split()
            d_keys[key] = value
    return d_keys


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


def co_en_vi(ch1, i_string, d_keys, s_key):
    f_dig = []
    s_dig = []
    th_dig = []
    for char in i_string:
        f_dig.append(d_keys[char])
    for char in s_key:
        s_dig.append(d_keys[char])
    for i in range(len(f_dig)):
        if ch1 == "1":
            th_dig.append(str((int(f_dig[i]) + int(s_dig[i])) % 37))
        if ch1 == "2":
            th_dig.append(str((int(f_dig[i]) - int(s_dig[i])) % 37))
    output_str = ""
    for char in th_dig:
        output_str = output_str + list(d_keys.keys())[list(d_keys.values()).index(char)]
    return output_str


def get_key_v23(i_string):
    flag = True
    while flag:
        print("Укажите букву-ключ\n")
        f_key = input().lower()
        s_key = f_key + i_string[:-1]
        if len(f_key) == 1:
            flag = False
    return [f_key, s_key]


def co_en_vi1(ch1, i_string, d_keys, keys):
    f_dig = []
    s_dig = []
    for char in i_string:
        f_dig.append(d_keys[char])
    for i in range(len(f_dig)):
        if ch1 == "1":
            if i == 0:
                s_dig.append(str((int(f_dig[i]) + int(d_keys[keys[0]])) % 37))
            else:
                s_dig.append(str((int(f_dig[i]) + int(s_dig[i - 1])) % 37))
        if ch1 == "2":
            if i == 0:
                s_dig.append(str((int(f_dig[i]) - int(d_keys[keys[0]])) % 37))
            else:
                s_dig.append(str((int(f_dig[i]) - int(s_dig[i - 1])) % 37))
    output_str = ""
    for char in s_dig:
        output_str = output_str + list(d_keys.keys())[list(d_keys.values()).index(char)]
    return output_str


def vigenere():
    flag = True
    while flag:
        print("Введите способ Виженера, которым хотите расшифровать/зашифровать текст:\n"
              "1. повторение короткого лозунга\n"
              "2. самоключ Виженера по открытому тексту\n"
              "3. самоключ Виженера по шифртексту\n")
        ch = input()
        if ch == "1" or ch == "2" or ch == "3":
            flag = False
    d_keys = o_keys_file("lists_of_ciphers/cipher1.txt")
    d_keys[" "] = "36"
    print("Введите предложение, которое хотите зашифровать/расшифровать")
    i_string = input().lower()
    if ch == "1":
        flag = True
        while flag:
            print("Укажите слово-ключ\n")
            f_key = input().lower()
            if len(f_key) < len(i_string):
                while len(f_key) < len(i_string):
                    f_key = 2*f_key
            if len(f_key) > len(i_string):
                f_key = f_key[:-(len(f_key) - len(i_string))]
            flag = False
        ch1 = co_or_en()
        if ch1 == "1":
            output_str = co_en_vi(ch1, i_string, d_keys, f_key)

        if ch1 == "2":
            output_str = co_en_vi(ch1, i_string, d_keys, f_key)
    if ch == "2":
        keys = get_key_v23(i_string)
        ch1 = co_or_en()
        if ch1 == "1":
            output_str = co_en_vi(ch1, i_string, d_keys, keys[1])
        if ch1 == "2":
            output_str = co_en_vi1(ch1, i_string, d_keys, keys)
    if ch == "3":
        ch1 = co_or_en()
        keys1 = get_key_v23(i_string)
        if ch1 == "1":
            output_str = co_en_vi1(ch1, i_string, d_keys, keys1)
        if ch1 == "2":
            output_str = co_en_vi(ch1, i_string, d_keys, keys1[1])
    print(output_str)
