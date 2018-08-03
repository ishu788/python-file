list=[]
e=[]
o=[]
for i in range(10):
      a=int(input())
      list.append(a)
for i in range (0,10):
      if(list[i]%2==0):
            a=list[i]
            e.append(a)
      else:
            a=list[i]
            o.append(a)
print(e)
print(o)


'''list=[]
n=int(input())
sum=0
for i in range(0,n):
      a=int(input())
      sum=sum+a
      list.append(a)
median=sum/n
print(median)
'''
