# List Methods

naturalNumbers = [23,65,12,24,87,44,32,89]
naturalNumbers.sort()
print(f"Sorting in Accending order :- {naturalNumbers}")
naturalNumbers.reverse()
print(f"Sorting in Decending order :- {naturalNumbers}")
naturalNumbers.append(58)
print(f"Adding number at the end of list :- {naturalNumbers}")
naturalNumbers.insert(2,43) # (index no. , value to be inserted)
print(f"Inserting number at the index 2 :- {naturalNumbers}")
naturalNumbers.pop(5) # index number
print(f"Taking out number of specified index from list :- {naturalNumbers}")
naturalNumbers.remove(44) # value to be removed
print(f"Removing number from list :- {naturalNumbers}")
