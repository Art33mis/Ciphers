import random as r
import math
import gmpy2
import numpy as np


def is_prime(n):
    if n % 2 == 0:
        return False
    for i in range(2, n - 1):
        ra = fast_pow(i, n - 1, n)
        if ra != 1:
            return False
    return True


def fast_pow(a, k, n):
    if (a < 0) or (k < 0) or (n <= 0):
        raise ValueError
    if (a >= n) or (k >= n):
        raise ValueError
    b = 1
    if k == 0:
        return b
    ki = list(np.binary_repr(k))
    ki.reverse()
    c = a
    if ki[0] == '1':
        b = a
    for i in range(1, len(ki)):
        c = c ** 2 % n
        if ki[i] == '1':
            b = (b * c) % n
    return b


def get_keys(ran):
    print("Выберите способ задания ключа:\n"
          "1. На основании введенных вами простых чисел\n"
          "2. Сгенерировать автоматически\n")
    in_str = input()
    if in_str == "1":
        print("Введите первое число")
        p = int(input())
        print("Введите второе число")
        q = int(input())
    if in_str == "2":
        flag = True
        while flag:
            p = r.randint(ran, ran * ran)
            q = r.randint(ran, ran * ran)
            if is_prime(p) and is_prime(q):
                flag = False
    n = p * q
    f = (p - 1) * (q - 1)
    for i in range(2, f):
        if math.gcd(i, f) == 1:
            e = i
            break
    for i in range(f * f):
        if (e * i) % f == 1:
            d = i
            break
    print(f"Ваш открытй ключ: {e} и {n}")
    print(f"Ваш закрытй ключ: {d}")
    return [e, n, d]


def code(m, e, n):
    c = fast_pow(m, e, n)
    return c


def encode(c, d, n):
    m = fast_pow(c, d, n)
    return m


def co_message():
    print("Введите предложение, которое хотите зашифовать")
    string = input().lower()
    print("Введите пару открытых ключей через пробел")
    keys = input().split()
    out = ' '.join(format(ord(x), 'b') for x in string)
    print(out)
    bin_arr = out.split()
    output = ""
    for char in bin_arr:
        output = output + str(code(int(char), int(keys[0]), int(keys[1]))) + " "
    print(output)
    return output


def en_message():
    print("Введите последовательность чисел, которую хотите расшифовать")
    string = input().lower()
    print("Введите пару открытых ключей и закрытый ключ через пробел")
    keys = input().split()
    bin_arr = string.split()
    inputs = ""
    for char in bin_arr:
        inputs = inputs + str(encode(int(char), int(keys[2]), int(keys[1]))) + " "
    print(inputs)
    revert = ''.join([chr(int(s, 2)) for s in inputs.split()])
    print(revert)
    return revert


def RSA():
    flag = True
    while flag:
        print("Нужно ли вам генерировать ключ?\n"
              "1. Да\n"
              "2. Нет\n")
        ch = input()
        if ch == "1" or ch == "2":
            flag = False
    if ch == "1":
        keys = get_keys(100)
    flag = True
    while flag:
        print("Что вы хотите сделать:\n"
              "1. Зашифровать\n"
              "2. Расшифровать\n")
        ch = input()
        if ch == "1" or ch == "2":
            flag = False
    if ch == "1":
        st = co_message()

    if ch == "2":
        en = en_message()


def hastad_attack(exp, n, c):
    t = []
    for i in range(exp):
        mod_prod = 1

        for j in range(exp):
            if i != j:
                mod_prod *= n[j]

        t_i = c[i] * mod_prod * gmpy2.invert(mod_prod, n[i])
        t.append(t_i)

    partial_total = 0
    mod_prod = 1
    for i in range(exp):
        partial_total += t[i]
        mod_prod *= n[i]

    message = str(gmpy2.iroot(partial_total % mod_prod, exp)[0])
    revert = ''.join([chr(int(s, 2)) for s in message.split()])
    return revert


