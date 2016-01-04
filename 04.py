# -*- coding: utf-8 -*-

import re

str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
ls = re.sub(r'\.',"",str).split(" ")

mem = [1,5,6,7,8,9,15,16,19]

dict = {}

for (s,n) in zip(ls, range(1,len(ls)+1)):
    if n in mem:
        dict[s[0:2]] = n
    else:
        dict[s[0:1]] = n

print dict
