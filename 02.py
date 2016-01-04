# -*- coding: utf-8 -*-

str1 = u"パトカー"
str2 = u"タクシー"

res = ""

for (a,b) in zip(str1, str2):
    res = res + a + b

print res.encode('utf-8')
