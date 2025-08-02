#WAP in python to filter number which is divisible by 5

l = [i for i in range(1,500)]
divisibleBy5 = list(filter(lambda x:x%5==0,l))
print(divisibleBy5)