#join method (Strings)
'''
join() works only on iterables of strings.

You must convert non-string elements (like numbers) before using join()

'''

clebs = ['Vicky Kausal','Kiara Advani']

couples = ' married with '.join(clebs)
print(couples)

owners=['Anita','Sabrina','Barkha','Monalisha']
Mobile_numbers =[6202490832,9876095644,6453908976,7250779087]

countryCode = ''.join('+91'+str(Mo_no)+'\n' for Mo_no in Mobile_numbers)
print(countryCode)

#format method -- old techniques
for i in range (0,len(owners)):
    OwnersNumbers = '{} -----+91-{}'.format(owners[i],Mobile_numbers[i] )
    print(OwnersNumbers)
print('||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
for i in range (0,len(owners)):
    OwnersNumbers = '+91-{1} ------{0}'.format(owners[i],Mobile_numbers[i] )
    print(OwnersNumbers)