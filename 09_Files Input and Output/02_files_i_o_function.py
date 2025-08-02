# functions in read write files.

f = open("/Users/assar/Desktop/Python Study/09_Files Input and Output/01_file.txt")
# lines = f.readlines() #--------> Read multiple lines in a list type
# print(lines,type(lines))
# f.close

# line1 = f.readline() #------> Reads single line at a time in string type
# print(line1,type(line1))

# line2 = f.readline() #------> Reads single line at a time in string type
# print(line2,type(line2))

# line3 = f.readline() #------> Reads single line at a time in string type
# print(line3,type(line3))

# f.close

# using while loop to read file 

line = f.readline()
while (line != ""):
    print(line)
    line=f.readline()

f.close

