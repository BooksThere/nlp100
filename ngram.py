def ngram(seq,n):
    res = []
    length = len(seq)
    if n <> 0 and length >= n:
        last = length - n
        for i in range(0, last + 1):
            res.append(seq[i:i+n])
    return res
