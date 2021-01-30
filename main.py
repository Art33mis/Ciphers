import affine
import affine_recurrent
import simple_replacement

if __name__ == '__main__':
    flag = True
    while flag:
        print("Выберите шифр, ктоорым хотите расшифровать или зашифровать файл\n"
              "1. Шифр простой замены\n"
              "2. Аффинный шифр\n"
              "3. Аффинный рекуррентный шифр\n")
        ch1 = input()
        if ch1 == "1" or ch1 == "2" or ch1 == "3":
            flag = False
    if ch1 == "1":
        simple_replacement.simple()
    if ch1 == "2":
        affine.affine()
    if ch1 == "3":
        affine_recurrent.recurrent()
