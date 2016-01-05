# -*- coding: utf-8 -*-

import sys
import codecs
import os

if __name__ == "__main__":
    param = sys.argv
    
    if len(param) == 3 and param[2].isdigit():
        fname = param[1]
        f = codecs.open(fname.encode('utf-8'), 'r', 'utf-8')

        n = int(param[2])
        if n > 0:
            c = 0
            files = []
            temp = ""

            for line in f:
                temp += line
                c += 1
                if c == n:
                    files.append(temp)
                    temp = ""
                    c = 0

            prefix,ext = os.path.splitext(fname)
            for i in range(0,len(files)):
                of = codecs.open((prefix + str(i) + ext).encode('utf-8'), 'w', 'utf-8')
                of.write(files[i])
