# -*- coding: utf-8 -*-

import random

def scrabble(str):
    length = len(str)
    if length < 5:
        return str
    else:
        ls = list(str[1:length-1:])
        random.shuffle(ls)
        return str[0] + "".join(ls) + str[length-1]

def scrabbles(str):
    ls = str.split(" ")
    return " ".join(map(scrabble,ls))

str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

print scrabbles(str)
