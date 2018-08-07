a= int(input())
b= int(input())
def check(a,b):
    x=int()
    x=a
    a=b
    b=x
    return a,b
print(check(a,b))
