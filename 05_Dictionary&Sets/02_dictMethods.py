#Methods of Dictionary

empty_dictionary = {} #Example of creation of empty dictionary
country_capital = {
    "India" : "Delhi",
    "USA" : "New York",
    "Japan" : "Tokyo",
    "Russia" : "Moscow",
    "China" : "Bejing"
}

print(country_capital.items())  #dict_items([('India', 'Delhi'), ('USA', 'New York'), ('Japan', 'Tokyo'), ('Russia', 'Moscow'), ('China', 'Bejing')]
print(country_capital.keys()) # dict_keys(['India', 'USA', 'Japan', 'Russia', 'China'])
print(country_capital.values()) #dict_values(['Delhi', 'New York', 'Tokyo', 'Moscow', 'Bejing'])
country_capital.update({"NewZealand" : "Auckland"})
print(country_capital) #{'India': 'Delhi', 'USA': 'New York', 'Japan': 'Tokyo', 'Russia': 'Moscow', 'China': 'Bejing', 'NewZealand': 'Auckland'}
print(country_capital.get("India")) #Delhi

# Difference between country_capital["India"] and country_capital.get("India") is that if no keys is found then country_capital.get("  ") will return none while country_capital[" "] will give error.

# country_capital.pop("China")
# print(country_capital)

country_capital.popitem() # It removes the last inserted key and value pair.
print(country_capital)

