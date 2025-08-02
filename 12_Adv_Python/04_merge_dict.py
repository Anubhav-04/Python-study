#merge dictionary
personalDetails = {
    'name':"Anubhav Kumar",
    'Age':28
}
officialDetails = {
    'Id':'ASSAR_0078',
    'Organization':'Assar'
}

empDetails = personalDetails | officialDetails

print(empDetails)

with (
    open("/Users/assar/Desktop/Python Study/09_Files Input and Output/01_file.txt") as f1,
    open("/Users/assar/Desktop/Python Study/09_Files Input and Output/write_file.txt") as f2
):
    print(f1.read())
    print('-------------------------------------------')
    print(f2.read())