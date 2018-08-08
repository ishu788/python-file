def adder(a, *b):
    sum = a
    for i in b:
        sum+=i
    return sum
print(adder(1))
print(adder(1,2))
print(adder(1,2,3))
print(adder(1,2,3,4))
