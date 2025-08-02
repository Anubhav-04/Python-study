from functools import reduce
#WAP in python to find the maximum of the number from the list

naturalNumbers = [5,3,4,2,6,4,8,9,4,10,23,7,1,0,2,5]
# def maxOfList(index,max):
#     if(index == len(naturalNumbers)):
#         return max
#     if(naturalNumbers[index]>max):
#         max = naturalNumbers[index]
#     return maxOfList(index+1,max)
# print(maxOfList(1,naturalNumbers[0]))

max = reduce(lambda a,b:a if a>b else b,naturalNumbers)
print(max)