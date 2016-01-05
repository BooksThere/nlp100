# -*- coding: utf-8 -*-

import re

str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
ls = re.sub(r'\.',"",str).split(" ")

mem = [1,5,6,7,8,9,15,16,19]

dict = {}
i = 0

for s in ls:
    i += 1
    if i in mem:
        dict[s[0:2]] = i
    else:
        dict[s[0:1]] = i

print dict
