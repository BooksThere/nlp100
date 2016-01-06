# -*- coding: utf-8 -*-

# sort -k 3,3 -r hightemp.txt 

import sys
import codecs

if __name__ == "__main__":
    param = sys.argv
    
    if len(param) == 2:
        fname = param[1]
        f = codecs.open(fname.encode('utf-8'), 'r', 'utf-8')

        lines = f.readlines()

        result = sorted(lines, key=lambda x:x.split("\t")[2], reverse=True)

        # debug print
        print "".join(result).encode('utf-8')
