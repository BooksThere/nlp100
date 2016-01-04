# -*- coding: utf-8 -*-

execfile('ngram.py')

strX = "paraparaparadise"
strY = "paragraph"

X = set(ngram(strX,2))
Y = set(ngram(strY,2))

print (X | Y), (X & Y), (X - Y), (Y - X), ("se" in X), ("se" in Y)
