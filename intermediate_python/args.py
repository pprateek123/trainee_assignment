def sum(*numbers):
    sum=0
    for item in numbers:
        sum+=item
    return sum

print(sum(1,2,3,4))
print(sum(3,4,5,6))
print(sum(10,10,10,10))
