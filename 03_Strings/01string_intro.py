#Introduction to String

chapter3 = "Introduction_to_Strings"

print (chapter3)

#String Slicing 

subString_of_chapter3 = chapter3[0:6] #Substring starts from index 0 and end at index 5 exluding index 6

print(subString_of_chapter3)

# if chapter3[:5] is like this it means chapter3[(0th index of the string):5]
# if chapter3[3:] is like this it means chapter3[3:(last index of the string)]

#String Slicing from last to first index
#last character of the String is considered as '-1' and gradually decreases to backward direction

negative_subString_of_chapter3 = chapter3[-21 : -11]

print(negative_subString_of_chapter3)

#String Slicing with skipping values

integers = "0123456789"

evenNumbers = integers[2:10:2]  # First recursion [2:10] 2345678 --> Second recursion [_:_:1]-- (Skipping the one character after first character) 2468 

oddNumbers = integers[1:11:2]

print("Even numbers among ",integers,"--->",evenNumbers)
print("Odd numbers among ",integers,"--->",oddNumbers)