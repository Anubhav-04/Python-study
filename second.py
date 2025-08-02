# '''
#     x     y      z         r
#  [0,1]  [0,1]  [0,1]   [[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]


# '''

# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
# list = []
# def createList(integer):
#     for i in range(0,integer+1):
#         list.append(i)
#     return list

# l1 = createList(x)
# print(f"list of x {l1}")
# list=[]
# l2 = createList(y)
# print(f"list of y {l2}")
# list=[]
# l3 = createList(z)
# print(f"list of z {l3}")

# print([l1,l2,l3])
# longList = []
# for i in range(0,x+1):
#     for j in range(0,y+1):
#         for k in range(0,z+1):
#             bigList = [l1[i],l2[j],l3[k]]
#             if(l1[i]+l2[j]+l3[k]!=n):
#                 longList.append(bigList)
# print(longList)

# # printing second largest
# scores = [3,9,8,10,4,6,8]

# uniqueNumbers = sorted(set(scores),reverse=True)
# print(uniqueNumbers)
# if len(uniqueNumbers) >= 2:
#     print(uniqueNumbers[1])

# listofstudents =[]
# for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         group = [name,score]
#         listofstudents.append(group)
# # print(listofstudents)

# # listofstudents = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

# uniqueMarks =[((listofstudents[i])[1]) for i in range(0,len(listofstudents))]
# # print(uniqueMarks)
# sort = sorted(set(uniqueMarks),reverse=True)
# # print(sort)
# a= len(sort)
# # print(a)
# if(len(sort)>=2):
#     secondLowestmarks = sort[a-2]
# # print(secondLowestmarks)
# dataOfSecondLargest = []
# for i in range(0,len(listofstudents)):
#       if((listofstudents[i])[1]==secondLowestmarks):
#         # print(listofstudents[i])
#         dataOfSecondLargest.append(listofstudents[i]) 
# # print(dataOfSecondLargest)

# names = [((dataOfSecondLargest[i])[0]) for i in range(0,len(dataOfSecondLargest))]

# nowSortNames = sorted(set(names),reverse=False)
# for i in nowSortNames:
#      print(i)

'''
4                                                               
Anubhav
25.78
Rani
37.99
Anurag
26.77
Anupama
26.77  

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti 
41
Harsh
39

'''

# n = int(input())
# student_marks = {}
# for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
# print(scores)
# print(student_marks)
# query_name = input()
# marks = student_marks[query_name]
# avg = 0
# for i in marks:
#         avg = avg + i
# print(f"{avg/3 :.2f}")

# a = int(input())
# rollNo1 = input().split(" ")
# b = int(input())
# rollNo2 = input().split(" ")

# set = set(rollNo1).intersection(set(rollNo2))
# print(set)
# i = 0
# for i in (0,len(set)):
#     k =i
#     i=i+1
# print(k)

# a = int(input())
# A = set(input().split(" "))
# n = int(input())
# str = []
# marks=[]
# for i in range(0,n):
#     U = input().split()
#     setU = input().split(" ")
#     str.append(U[0])
#     marks.append(setU)
# print(str)
# print(marks)
# l1 =marks[0]
# l2 =marks[1]
# l3 = marks[2]
# l4 = marks[3]
# print(l1)
# print(l2)
# print(l3)
# print(l4)
# B = C = D = E = set()
# for i in range (0,n):
#     if(str[i] == "intersection_update"):
#         A.intersection_update(set(marks[i])) 
#     elif(str[i] == "update"):
#         A.update(set(marks[i]))
#     elif(str[i] == "symmetric_difference_update"):
#         A.symmetric_difference_update(set(marks[i]))
#     elif(str[i]=="difference_update"):
#         A.difference_update(set(marks[i]))
# # print(A)
# a = 0
# for i in A:
#     a = int(i) + a
# print(a)
# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 24, 52]
# l2 = [2,3,5,6,8,9,1,4,7,11]
# s = set(l1)
# s.intersection_update(set(l2))
# print(s)



'''
16
1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
4
intersection_update 10
2 3 5 6 8 9 1 4 7 11
update 2
55 66
symmetric_difference_update 5
22 7 35 62 58
difference_update 7
11 22 35 55 58 62 66

'''
'''
from collections import Counter 
roomNumbers = [1, 2, 3, 6, 5, 4, 4, 2, 5, 3, 6,1, 6, 5, 3, 2, 4, 1, 2, 5, 1, 4, 3, 6, 8, 4, 3, 1, 5, 6, 2]
a = Counter(roomNumbers)
print(a)

freq = {}
for i in roomNumbers:
    if(i in freq):
        freq[i] += 1
    else:
        freq[i] =1

for key,value in freq.items():
    if(value==1):
        print(key)

'''

if __name__ == '__main__':
    n = int(input())
    my_list = []
    for i in range(n):
        inputElement = input().split()
        command = inputElement[0]
        args = list(map(int, inputElement[1:]))  # Convert arguments to integers

        if command == 'insert':
            my_list.insert(args[0], args[1])
        elif command == 'remove':
            my_list.remove(args[0])
        elif command == 'append':
            my_list.append(args[0])
        elif command == 'sort':
            my_list.sort()
        elif command == 'pop':
            my_list.pop()
        elif command == 'reverse':
            my_list.reverse()
        elif command == 'print':
            print(my_list)

        
    
