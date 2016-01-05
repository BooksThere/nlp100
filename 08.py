# -*- coding: utf-8 -*-

import re

def cipher_aux(c):
    if re.compile("[a-z]").search(c):
        return chr(219 - ord(c))
    else:
        return c
        
def cipher(str):
    return "".join(map(cipher_aux,str))

str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

print cipher(str)
