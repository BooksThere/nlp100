# -*- coding: utf-8 -*-

# wc -l hightemp.txt

import sys
import codecs

if __name__ == "__main__":
    param = sys.argv
    
    if len(param) == 2:
        fname = param[1]
        f = codecs.open(fname.encode('utf-8'), 'r', 'utf-8')

        ln = 0

        for line in f:
            ln += 1

        print ln

