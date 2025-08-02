# WAP in python to detect spam messages if it contains 
# "Make a lot of money $$$$"
# "Buy Now!!!"
# "Subscribe This"
# "Click on this"
message = input("Enter your message - ")
statement = ["Make a lot of money $", "Buy Now!!!", "Subscribe This","Click on this"]
if(statement[0] in message or statement[1] in message or statement[2] in message or statement[3] in message):
    print("It's a spam!!!")
else:
    print("No Spam")