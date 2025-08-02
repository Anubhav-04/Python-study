from functools import reduce
# MAP example

l = [9,5,3,7,2,6]

cubesFunc = lambda x:x**3

cubesofL = map(cubesFunc,l)
print(list(cubesofL))

squred = map(lambda x:x**2,l)
print(list(squred))

# Filter example

evenNos = list(filter(lambda x:x%2==0,l))
print(evenNos)

oddNos = list(filter(lambda x:x%2!=0,l))
print(oddNos)

#Reduce example

sum = reduce(lambda x,y:x+y,l)
print(sum)

mul = reduce(lambda x,y:x*y,l)
print(mul)