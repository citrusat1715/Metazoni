def grouped(l, n):
    for i in (0, len(l), n):
        yield l[i:i+n]
