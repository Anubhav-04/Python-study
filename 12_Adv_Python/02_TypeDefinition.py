from typing import List,Tuple,Dict,Union

# List of integers

numbers :List[int] = [1,2,3,6,9]
print(numbers)

# Tuple of integers and strings

age : Tuple[str,int] = ('Alice',21)
print(age)

# Dictionary of string and integer

tele : Dict[str,int]
# Type Definition


n : int = 5   # Explicitly defining the type of variable

print(n.is_integer())

name : str = "Anubhav" # Explicitly defining the type of variable
print(type(name))

def sum (a :int , b:int) -> int: # Explicitly defining the
    # variable types and return type in the function definition
    print(a+b)
sum(5,6)