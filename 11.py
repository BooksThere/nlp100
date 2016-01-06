# -*- coding: utf-8 -*-

# tr '\t' ' ' < hightemp.txt

import re
import sys
import codecs

if __name__ == "__main__":
    param = sys.argv
    
    if len(param) == 2:
        fname = param[1]
        f = codecs.open(fname.encode('utf-8'), 'r', 'utf-8')

        result = ""
        for line in f:
            result += re.sub(r'\t',' ',line.encode('utf-8'))

        print result
