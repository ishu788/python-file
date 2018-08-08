n = int(input())
def avg(n):
    sum=0
    for i in range (1,n+1):
        sum = sum+i
    avg = sum/n
    return avg
print(avg(n))
