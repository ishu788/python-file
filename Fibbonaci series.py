n1=0
n2=1
count=0
list= []

x = int(input("how many terms"))

if x<=0:
    print("enter a positive no.")
elif x ==1:
    print("fibonaci series:")
    print(n1)
else:
    print("fibonacci series:")
    while count<x:
          list.append(n1) 
          nn = n1+n2
          n1=n2
          n2=nn
          count +=1
print(list)
