def ngram(seq,n):
    res = []
    length = len(seq)
    if length < n:
        return res
    else:
        last = length - n
        for i in range(0, last + 1):
            res.append(seq[i:i+n])
        return res
