# Problem 3 :- WAP in Python to detect double space in String

problem = "Python  to detect double space in String"

print(problem.find("  "))

# Problem 4 :- Replacing the double space with single space
# print(problem)
print(problem.replace("  "," "))

#Problem 5 : Format the following sentence using escape sequence

letter = "Dear Python user, Please rate the Visual Studio CodeShare your experience.Regards"
formatted_letter = "Dear Python user,\n\tPlease rate the \"Visual Studio Code\"\n\tShare your experience.\nRegards"
print(letter)
print(formatted_letter)