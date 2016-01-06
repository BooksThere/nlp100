# -*- coding: utf-8 -*-

# sort col1.txt | uniq

import sys
import codecs

if __name__ == "__main__":
    param = sys.argv
    
    if len(param) == 2:
        fname = param[1]
        f = codecs.open(fname.encode('utf-8'), 'r', 'utf-8')

        col1 = []

        for line in f:
            strs = line.split("\t")
            col1.append(strs[0])

        colset = set(col1)

        # debug print
        print "\n".join(list(colset)).encode('utf-8')
