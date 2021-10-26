#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def min_max(args):

    # Ищет максимальный аргумет
    for i, item in enumerate(args):
        if item == '(':

            # После максимального элемента умножает все элементы
            for value in args[i+1:]:
                if value == ')':
                    return True

     return min_max(args)


if __name__ == '__main__':
    arg = input('Введите список аргументов: ')
    print("Результат: ")
    print(min_max(arg))
