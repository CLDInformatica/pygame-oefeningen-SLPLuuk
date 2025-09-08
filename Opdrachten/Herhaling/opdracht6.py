# Maak een functie genaamd rekenmachine met 3 argumenten:

#   - getal1
#   - getal2
#   - operatie

# De operatie kan plus, min, keer of delen zijn. 

# Doe iets met getal1 en getal2 afhankelijk van de operatie en return het resultaat.
# Dus als operatie plus is tel je de 2 getallen bij elkaar op, enz.
# Voer hierna de functie uit met verschillende inputs en bekijk de resultaten.
# Let op: Het is verplicht om een functie te gebruiken!

def rekenmachine(getal1, getal2, operatie):
    if operatie == "+" or "-" or "/" or "*":
        if operatie == "+":
            return(getal1 + getal2)
        elif operatie == "-":
            return(getal1 - getal2)
        elif operatie == "/":
            return(getal1 / getal2)
        elif operatie == "*":
            return(getal1 * getal2)
    else:
        print("nee")
    
c = rekenmachine(2, 200, "+")
print(c)
