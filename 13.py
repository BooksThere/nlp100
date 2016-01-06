# -*- coding: utf-8 -*-

# paste col1.txt col2.txt

import codecs

if1 = codecs.open('col1.txt', 'r', 'utf-8')
if2 = codecs.open('col2.txt', 'r', 'utf-8')

col1 = []
col2 = []

for l1 in if1:
    col1.append(l1.rstrip().encode('utf-8'))

for l2 in if2:
    col2.append(l2.rstrip().encode('utf-8'))

result = "\n".join(map(lambda (x, y): x + '\t' + y, zip(col1,col2))) + "\n"

of = codecs.open('cols.txt', 'w', 'utf-8')
of.write(result.decode('utf-8'))
    
    
