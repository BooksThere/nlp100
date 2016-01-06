# -*- coding: utf-8 -*-

# cut -f 1 hightemp.txt | sort | uniq -c | sort -r | cut -c 6-

import sys
import codecs
import collections

if __name__ == "__main__":
    param = sys.argv
    
    if len(param) == 2:
        fname = param[1]
        f = codecs.open(fname.encode('utf-8'), 'r', 'utf-8')

        lines = f.readlines()
        splits = map(lambda line:line.split("\t"), lines)

        # 各県名の出現回数を計測
        col1 = map(lambda x:x[0], splits)
        cnt = collections.Counter(col1)

        result = "\n".join(map(lambda (x,y):x,cnt.most_common()))

        print result.encode('utf-8')
