# Python formatting using format()

amount = 150.75

print("Amount ${:.2f}".format(amount))

# Python formatting using sep and end parameter

#Using end='@'
print("Python" ,end='@')
print("GeeksForGeeks")

#Using sep
print("G","F","G" , sep=' ')
#Date formatting
print("09","06","2025" , sep='/')
print("Anubhav", "geeksforgeeks" ,sep='@')

#Using f string

name="Anubhav"
Age= 28
print(f"Hello My name is {name} and i am {Age} years old.")

#Using % operator

# %d – integer
# %f – float
# %s – string
# %x – hexadecimal
# %o – octal

num = 45
add = num+5
print("The sum is %d" %add)