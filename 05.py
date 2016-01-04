# -*- coding: utf-8 -*-

execfile('ngram.py')
# def ngram(seq,n):
#     res = []
#     length = len(seq)
#     if length < n:
#         return res
#     else:
#         last = length - n
#         for i in range(0, last + 1):
#             res.append(seq[i:i+n])
#         return res

str = "I am NLPer"

import re

print ngram(str.split(" "),2), ngram(re.sub(r' ',"",str),2)
