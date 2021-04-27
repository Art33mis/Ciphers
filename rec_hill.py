import numpy as np
from numpy import linalg as la


def o_keys_file(cipher):
    d_keys = {}
    with open(cipher) as file:
        for line in file:
            key, value = line.split()
            d_keys[key] = value
    return d_keys


def get_key_h(ch, l_key=0):
    flag = True
    while flag:
        print("Укажите слово-ключ\n"
              "Его длина должна равняться квадрату целого числа")
        s_key1 = input().lower()
        l_key1 = len(s_key1) ** 0.5
        i_key1 = int(l_key1)
        if ch == 1:
            if l_key1 == i_key1:
                flag = False
        if ch == 2:
            if l_key1 == i_key1 and l_key == l_key1:
                flag = False
    return [l_key1, s_key1]


def get_array(i_string, l_key1, d_keys, ch=0):
    f_dig = []
    s_dig = []
    counter = 0
    for char in i_string:
        if counter < l_key1:
            f_dig.append(int(d_keys[char]))
            counter += 1
        else:
            counter = 1
            s_dig.append(f_dig.copy())
            f_dig.clear()
            f_dig.append(int(d_keys[char]))
    if ch == 1:
        if len(f_dig) < l_key1:
            while len(f_dig) < l_key1:
                f_dig.append(36)
    s_dig.append(f_dig)
    return s_dig


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


def co_en_hill(d_keys, key1, s_dig):
    f_string = ""
    for i in range(len(s_dig)):
        s_dig[i] = (np.dot(s_dig[i], key1)) % 37
        for j in range(len(s_dig[i])):
            symbol = list(d_keys.keys())[list(d_keys.values()).index(str(int(s_dig[i][j])))]
            f_string = f_string + str(symbol)
    return f_string


def get_r_key_h(key1):
    det = round(la.det(key1))
    for i in range(1000):
        if (det * i) % 37 == 1:
            r_det = i
            break
    inv_key1 = (la.inv(key1) * det * r_det)
    inv_key1 = np.around(inv_key1 % 37)
    return inv_key1


def rec_hill():
    d_keys = o_keys_file("lists_of_ciphers/cipher1.txt")
    d_keys[" "] = "36"
    f_key1 = get_key_h(1)
    f_key2 = get_key_h(2, f_key1[0])
    s_dig1 = get_array(f_key1[1], f_key1[0], d_keys)
    key1 = np.array(s_dig1)
    s_dig2 = get_array(f_key2[1], f_key2[0], d_keys)
    key2 = np.array(s_dig2)
    ch1 = co_or_en()
    if ch1 == "1":
        print("Введите предложение, которое хотите зашифровать")
        i_string = input().lower()
        a_keys = [key1, key2]
        s_dig = get_array(i_string, f_key1[0], d_keys, 1)
        for i in range(len(s_dig)):
            if i > 1:
                a_keys.append(np.dot(a_keys[i - 1], a_keys[i - 2]))
        f_string = ""
        for i in range(len(s_dig)):
            s_dig[i] = (np.dot(s_dig[i], a_keys[i])) % 37
            for j in range(len(s_dig[i])):
                symbol = list(d_keys.keys())[list(d_keys.values()).index(str(s_dig[i][j]))]
                f_string = f_string + str(symbol)
    if ch1 == "2":
        print("Введите предложение, которое хотите зашифровать")
        i_string = input().lower()
        inv_key1 = get_r_key_h(key1)
        inv_key2 = get_r_key_h(key2)
        p_keys = [inv_key1, inv_key2]
        s_dig = get_array(i_string, f_key1[0], d_keys, 1)
        for i in range(len(s_dig)):
            if i > 1:
                p_keys.append((np.dot(p_keys[i - 2], p_keys[i - 1])))
        f_string = ""
        for i in range(len(s_dig)):
            s_dig[i] = (np.dot(s_dig[i], p_keys[i])) % 37
            for j in range(len(s_dig[i])):
                symbol = list(d_keys.keys())[list(d_keys.values()).index(str(int(s_dig[i][j])))]
                f_string = f_string + str(symbol)

    print(f_string)
