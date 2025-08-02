# WAP in python to open three different files file1.txt 
# file2.txt and file3.txt if any of the file is 
# not present a message must be promted without 
# exiting the same
try:
    with(
        open('/Users/assar/Desktop/Python Study/12_Adv_Python/12_Practice Set CH-12/file1.txt','r') as f1,
        open('/Users/assar/Desktop/Python Study/12_Adv_Python/12_Practice Set CH-12/file2.txt','r') as f2,
        open('/Users/assar/Desktop/Python Study/12_Adv_Python/12_Practice Set CH-12/file3.txt','r') as f3
    ):
        content1 = f1.read()
        content2 = f2.read()
        content3 = f3.read()
        print(content1)
        print(content2)
        print(content3)
except FileNotFoundError:
    print("File not found Error")
finally:
    try:
        f1.close()
        f2.close()
        f3.close()
        print("Files are closed")
    except NameError:
            print("No file was opened so not closed")
