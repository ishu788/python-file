b = int(input())
a = int(input())
def hyp(a,b):
    b = b**2
    a = a**2
    hyp = b+a
    h = hyp**.5
    return h
print(hyp(a,b))
