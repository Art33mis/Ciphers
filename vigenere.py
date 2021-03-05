import common


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
    d_keys = common.o_keys_file("lists_of_ciphers/cipher1.txt")
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
        ch1 = common.co_or_en()
        if ch1 == "1":
            output_str = common.co_en_vi(ch1, i_string, d_keys, f_key)

        if ch1 == "2":
            output_str = common.co_en_vi(ch1, i_string, d_keys, f_key)
    if ch == "2":
        keys = common.get_key_v23(i_string)
        ch1 = common.co_or_en()
        if ch1 == "1":
            output_str = common.co_en_vi(ch1, i_string, d_keys, keys[1])
        if ch1 == "2":
            output_str = common.co_en_vi1(ch1, i_string, d_keys, keys)
    if ch == "3":
        ch1 = common.co_or_en()
        keys1 = common.get_key_v23(i_string)
        if ch1 == "1":
            output_str = common.co_en_vi1(ch1, i_string, d_keys, keys1)
        if ch1 == "2":
            output_str = common.co_en_vi(ch1, i_string, d_keys, keys1[1])
    print(output_str)


