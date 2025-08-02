#WAP in python to censor multiple words from the file.txt

words = ['hell','jerk','crap','ass','idiot','moron','shitty','bullshit','screw-up','pissing','fool']

with open("/Users/assar/Desktop/Python Study/09_Files Input and Output/09_Practice Set CH-9/05_censor.txt","r") as r:
    content = r.read()
for word in words:
    content = content.replace(word,"#"*len(word))
    with open("/Users/assar/Desktop/Python Study/09_Files Input and Output/09_Practice Set CH-9/05_censor.txt","w") as w:
        w.write(content)
