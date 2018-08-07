a= int(input())
b= int(input())
c= int(input())

def avg(a,b,c):
    avg=int()
    avg=(a+b+c)/3
    if(avg%2==0):
        return "even"
    else:
        return "odd"
print(avg(a,b,c))
