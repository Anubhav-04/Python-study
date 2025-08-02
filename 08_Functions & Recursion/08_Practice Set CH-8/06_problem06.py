#WAP in python to remove any item from the list by creating a function.

planets = ["Mercury","Venus","Earth","Mars","Jupitar","Saturn","Uranus","Neptune","Pluto"]

def removeDwarf(planets,dwarf):
    for item in planets:
        if(item==dwarf):
            planets.remove(dwarf)
    return planets
dwarfPlanet = input("Enter the name of dwarf planet:- ")
print(removeDwarf(planets,dwarfPlanet))