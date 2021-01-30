import common


def affine():
    print("Укажите количество слов в вашем алфавите")
    alpha_count = int(input())
    d_keys = common.o_keys_file("cipher1.txt")
    key1 = common.get_key1(alpha_count)
    key2 = common.get_key2(alpha_count)
    ch1 = common.co_or_en()
    if ch1 == "1":
        print("Введите предложение, которое хотите зашифровать")
        f_string = common.co_en_aff(d_keys, ch1, key1, key2, alpha_count)
    if ch1 == "2":
        r_key1 = common.get_r_key(key1, alpha_count)
        print("Введите предложение, которое хотите расшифровать")
        f_string = common.co_en_aff(d_keys, ch1, r_key1, key2, alpha_count)
    print(f_string)

