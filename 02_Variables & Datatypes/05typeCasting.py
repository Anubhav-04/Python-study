#type() function and typecasting

a = 123
name="Anubhav"
dec=1.414
isTrue=True
nothing=None
wType1 = type(a)        # <class 'int'>
wType2 = type(name)     #<class 'str'>
wType3 = type(dec)      #<class 'float'>
wType4 = type(isTrue)   #<class 'bool'>
wType5 = type(nothing)  #<class 'NoneType'>
print(wType1)
print(wType2)
print(wType3)
print(wType4)
print(wType5)

#Typecasting or type conversion
b=str(143)
c=float(45)
d=int(3.14)

print(b, c, d)
