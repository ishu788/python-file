a= int(input())
b= int(input())
def check(a,b):
    if(a==b):
        z="Equal"
        return z
    elif(a>b):
        z="a greater"
        return z
    else:
        z="b greater"
        return z
print(check(a,b))
