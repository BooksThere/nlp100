# -*- coding: utf-8 -*-

# head -n N hightemp.txt

import sys
import codecs

if __name__ == "__main__":
    param = sys.argv
    
    if len(param) == 3 and param[2].isdigit():
        fname = param[1]
        f = codecs.open(fname.encode('utf-8'), 'r', 'utf-8')

        n = int(param[2])
        c = 0
        
        for line in f:
            if n <= c:
                break
            c += 1
            print line.rstrip().encode('utf-8')
