# Sets in Python

empty_set = set()  #Creating empty set

prime_numbers = {2,3,5,7,11}

print(prime_numbers,type(prime_numbers)) #{2, 3, 5, 7, 11} <class 'set'>

#Methods of Sets in Python

prime_numbers.add(27)
print(prime_numbers) #{2, 3, 5, 7, 27, 11}

prime_numbers.remove(11)
print(prime_numbers)

prime_numbers.pop() #Removes random element from set
print(prime_numbers)

print(len(prime_numbers))

prime_numbers.clear() # Clears the set
print(prime_numbers)

# Union & Intersection in Sets

natural_number = {1,2,3,4,5,6,7,8,9,10}
even_numbers = {2,4,6}
odd_numbers = {3,7,11}

print(natural_number.union(odd_numbers)) #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

print(even_numbers.union(odd_numbers)) #{2, 3, 4, 6, 7, 11}

print(natural_number.intersection(even_numbers)) #{2, 4, 6}

print(even_numbers.intersection(odd_numbers)) #set() empty set 

# Subset and Super set

print(natural_number.issuperset(even_numbers)) #True

print(even_numbers.issubset(natural_number)) #True

print(odd_numbers.issubset(natural_number)) #False

print(odd_numbers - natural_number) # {11}

print(natural_number.difference(odd_numbers)) #{1, 2, 4, 5, 6, 8, 9, 10}