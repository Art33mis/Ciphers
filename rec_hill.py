import numpy as np
import common


def rec_hill():
    d_keys = common.o_keys_file("lists_of_ciphers/cipher1.txt")
    d_keys[" "] = "36"
    f_key1 = common.get_key_h(1)
    f_key2 = common.get_key_h(2, f_key1[0])
    s_dig1 = common.get_array(f_key1[1], f_key1[0], d_keys)
    key1 = np.array(s_dig1)
    s_dig2 = common.get_array(f_key2[1], f_key2[0], d_keys)
    key2 = np.array(s_dig2)
    ch1 = common.co_or_en()
    if ch1 == "1":
        print("Введите предложение, которое хотите зашифровать")
        i_string = input().lower()
        a_keys = [key1, key2]
        s_dig = common.get_array(i_string, f_key1[0], d_keys, 1)
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
        inv_key1 = common.get_r_key_h(key1)
        inv_key2 = common.get_r_key_h(key2)
        p_keys = [inv_key1, inv_key2]
        s_dig = common.get_array(i_string, f_key1[0], d_keys, 1)
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
