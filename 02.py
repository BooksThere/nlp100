# -*- coding: utf-8 -*-

str1 = u"パトカー"
str2 = u"タクシー"

res = reduce(lambda l,(a,b): l + a + b, zip(str1, str2),"")

print res.encode('utf-8')
