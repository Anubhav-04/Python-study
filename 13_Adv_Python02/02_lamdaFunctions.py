#Lambda Functions
#lambda functions are created using an expression using 'lambda' keyword

square = lambda x:x*x
print(square(6))

list = lambda a,b,c,d:[a*b,b*c,c*d,b*d,c*d,c*a,d*a]
print(list(5,6,7,8))
numbers=[5,3,9,4,2,8,7]
sort = sorted(numbers, key=lambda x:x)
print(sort)