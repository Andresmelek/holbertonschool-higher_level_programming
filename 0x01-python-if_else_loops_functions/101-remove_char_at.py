#!/usr/bin/python3
def remove_char_at(str, n):
    str1 = ''
    index = 0
    for i in str:
        if index == n:
            index += 1
        else:
            str1 += chr(ord(i))
            index += 1
    return str1
