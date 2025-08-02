# WAP in python to replace the word idiot with ##### from a 04_sample.txt file.

word = "idiot"
with open("/Users/assar/Desktop/Python Study/09_Files Input and Output/09_Practice Set CH-9/04_sample.txt","r") as r:
    content = r.read()
newContent = content.upper().replace(word.upper(),"#####")
       
with open("/Users/assar/Desktop/Python Study/09_Files Input and Output/09_Practice Set CH-9/04_sample.txt","w") as w:
    w.write(newContent.capitalize())
 
