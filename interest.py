p= int(input())
t= int(input())

def interest(p,t):
    z = int(input("enter age"))
    if(z>65):
        r= float(.12)
        ggrate= float((p*r*t)/100)
        return ggrate
    else:
        r=float(.1)
        ggrate= float((p*r*t)/100)
        return ggrate
print(interest(p,t))

