#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    option = str(input(
        "Введите, как заполнить кортеж: \"Вручную\" или \"Автоматически\"\n"))
    if option.lower() == "вручную":
        A = list(map(int, input().split()))
    else:
        A = (76, 76, 76, 54, 62, 14, 102, 43)
    print("Введенные значения: ", *A)

    i = 1
    pos = 0
    while (i <= len(A)) and (pos != len(A)):
        i += 1
        pos += 1
        break

    i = 1
    pos = 0
    try:
        while (i <= len(A)) and (A[0] == A[i]):
            i += 1
            pos += 1
    except IndexError:
        print("В кортеже все значения одинаковые!", file=sys.stderr)
        exit(1)
    print("Количество равных элементов в начале: ", pos + 1)
    print("Элементы, стоящие после равных элементов: ", *A[pos + 1:])
