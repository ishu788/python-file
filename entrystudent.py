n = int(input())
dict = {}
dict1 = {}
for i in range(n):
    x=input()
    z=int(input())
    z1=int(input())
    z2=int(input())
    z3=int(input())
    dict[x]= z,z1,z2,z3
    dict1[x]= z+z1+z2+z3
print(dict)
print(dict1)
