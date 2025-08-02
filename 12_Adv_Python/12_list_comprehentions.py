#list comprehentions

numbers = [3,5,7,2,9]

squaredNumbers = [i*i for i in numbers]
cubeNumbers = [i*i*i for i in numbers]

print(squaredNumbers)
print(cubeNumbers)

heroineName = ['Shilpa','Sonam','Rani','Preety']
heroineTitles =['Shetty','Kapoor','Mukherjee','Zinta']

# for i in range(0,len(heroineName)):
#     heroinesFullNames = f"{heroineName[i]} {heroineTitles[i]}"
#     print(heroinesFullNames)

heroinesFullNames = [f"{heroineName[i]} {heroineTitles[i]}" for i in range(0,len(heroineName))]
print(heroinesFullNames)

