#WAP in Python to print the user entered name along with good afternoon using input()

from datetime import date

wName = input("What is your name :- ")
greet = "Good Afternoon"

print ("Hello Mr.",wName,greet)

# Problem 2


today= date.today()

# print ("Dear",wName,"\nYou Are Selected !!! \nDate -",today)

print (f"Dear {wName}\nYou Are Selected !!! \nDate -{today}")

letter = '''Dear <|Name|>
We are pleased to inform you that
your connection to jio home is
restored.
Thankyou <|Provider|>
Dated :- <|Date|>
'''

print(((letter.replace("<|Name|>","Anubhav Kumar Gupta")).replace("<|Provider|>", "Jio Network")).replace("<|Date|>","30 April 2025"))
