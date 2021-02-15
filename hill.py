import numpy as np
from numpy import linalg as la
import common


def hill():
    d_keys = common.o_keys_file("cipher1.txt")
    d_keys[" "] = "36"
    key = common.get_key_h(1)
    s_dig = common.get_array(key[1], key[0], d_keys)
    key1 = np.array(s_dig)
    ch1 = common.co_or_en()
    if ch1 == "1":
        print("Введите предложение, которое хотите зашифровать")
        i_string = input().lower()
        s_dig = common.get_array(i_string, key[0], d_keys, 1)
        f_string = common.co_en_hill(d_keys, key1, s_dig)
    if ch1 == "2":
        print("Введите предложение, которое хотите расшифровать")
        i_string = input().lower()
        inv_key1 = common.get_r_key_h(key1)
        s_dig = common.get_array(i_string, key[0], d_keys, 1)
        f_string = common.co_en_hill(d_keys, inv_key1, s_dig)
    print(f_string)









