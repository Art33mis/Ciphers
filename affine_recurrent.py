import common


def recurrent():
    print("Укажите количество слов в вашем алфавите")
    alpha_count = int(input())
    d_keys = common.o_keys_file("cipher1.txt")
    key1 = common.get_key1(alpha_count)
    key2 = common.get_key1(alpha_count)
    key3 = common.get_key2(alpha_count)
    key4 = common.get_key2(alpha_count)
    ch1 = common.co_or_en()
    if ch1 == "1":
        print("Введите предложение, которое хотите зашифровать")
        common.co_en_rec(d_keys, ch1, key1, key2, key3, key4, alpha_count)
    if ch1 == "2":
        r_key1 = common.get_r_key(key1, alpha_count)
        r_key2 = common.get_r_key(key2, alpha_count)
        print("Введите предложение, которое хотите расшифровать")
        common.co_en_rec(d_keys, ch1, r_key1, r_key2, key3, key4, alpha_count)

