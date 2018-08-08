def simple_interest(p,r,t,**kwargs):
    si= p*r*t/100
    print(si)
    for r,v in kwargs.items():
        print(r,v)
print(simple_interest(p=1000,r=5,t=10,p1=10000,p2=20000,r1=7,r2=8,t1=20,t2=5))
