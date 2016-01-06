# -*- coding: utf-8 -*-

# cut -f 1 < hightemp.txt 
# cut -f 2 < hightemp.txt 

import sys
import codecs

if __name__ == "__main__":
    param = sys.argv
    
    if len(param) == 2:
        fname = param[1]
        f = codecs.open(fname.encode('utf-8'), 'r', 'utf-8')

        col1 = []
        col2 = []

        for line in f:
            strs = line.split("\t")
            col1.append(strs[0])
            col2.append(strs[1])

        result1 = "\n".join(col1) + "\n"
        result2 = "\n".join(col2) + "\n"

        of1 = codecs.open('col1.txt', 'w', 'utf-8')
        of2 = codecs.open('col2.txt', 'w', 'utf-8')

        of1.write(result1)
        of2.write(result2)

