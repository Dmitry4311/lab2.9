#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def brackets_check(s, meetings=0):
    if meetings < 0:
        return False
    if s:
        if s[0] == '(':
            meetings += 1
        elif s[0] == ')':
            meetings -= 1
        return brackets_check(s[1:], meetings)
    return meetings == 0


if __name__ == '__main__':
    if brackets_check(input("Введите скобочную последовательность: ")):
        print('True')
    else:
        print('False')
