# Read file in python
read_file = open("/Users/assar/Desktop/Python Study/09_Files Input and Output/01_file.txt","r")
content = read_file.read()
print(content)
# Close the file after reading
read_file.close()

# Write file in python
st = "Ramayna and Mahabharta is a great epic in the world."
make_file = open("/Users/assar/Desktop/Python Study/09_Files Input and Output/write_file.txt","w")
make_file.write(st)
make_file.close

#read line in python

f = open("/Users/assar/Desktop/Python Study/09_Files Input and Output/01_file.txt","r")
print(f.readline())
f.close



