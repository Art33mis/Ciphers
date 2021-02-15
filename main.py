import affine
import affine_recurrent
import simple_replacement
import hill
import rec_hill


def main():
    flag = True
    while flag:
        print("Выберите шифр, ктоорым хотите расшифровать или зашифровать файл\n"
              "1. Шифр простой замены\n"
              "2. Аффинный шифр\n"
              "3. Аффинный рекуррентный шифр\n"
              "4. Шифр Хилла"
              "5. Рекуррентный шифр Хилла")
        ch1 = input()
        if ch1 == "1" or ch1 == "2" or ch1 == "3" or ch1 == "4" or ch1 == "5":
            flag = False
    if ch1 == "1":
        simple_replacement.simple()
    if ch1 == "2":
        affine.affine()
    if ch1 == "3":
        affine_recurrent.recurrent()
    if ch1 == "4":
        hill.hill()
    if ch1 == "5":
        rec_hill.rec_hill()


main()
