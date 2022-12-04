#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    option = str(input(
        "Введите, как заполнить кортеж: \"Вручную\" или \"Автоматически\"\n"))
    if option.lower() == "вручную":
        print("Введите значения через пробел: ")
        A = list(map(int, input().split()))
        if (len(A) == 0):
            print("В кортеже нет значений!", file=sys.stderr)
            exit(1)
    else:
        A = (76, 76, 76, 54, 62, 14, 102, 43)
    print("Введенные значения: ", *A)

    i = 1
    pos = 0
    # Обработка ошибки одинаковых значений (выход за границу)
    try:
        # Пока не дошли до конца кортежа и нулевой элемент равен следующим
        while (i <= len(A)) and (A[0] == A[i]):
            i += 1
            pos += 1
    except IndexError:
        print("В кортеже все значения одинаковые!", file=sys.stderr)
        exit(1)
    print("Количество равных элементов в начале: ", pos + 1)
    print("Элементы, стоящие после равных элементов: ", *A[pos + 1:])
