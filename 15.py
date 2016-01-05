# -*- coding: utf-8 -*-

import sys
import codecs

if __name__ == "__main__":
    param = sys.argv
    
    if len(param) == 3 and param[2].isdigit():
        fname = param[1]
        f = codecs.open(fname.encode('utf-8'), 'r', 'utf-8')

        n = len(f.readlines()) - int(param[2])
        c = 0

        f.seek(0)
        for line in f:
            if n <= c:
                print line.rstrip().encode('utf-8')
            c += 1
