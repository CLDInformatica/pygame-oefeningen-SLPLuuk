# Gegeven is een functie met 2 argumenten:
#   - getal1
#   - getal2

# Return de grootste van deze 2 getallen.
# Voer de functie daarna uit met verschillende waarden en print de uitkomst

def grootste(getal1, getal2):
    if getal1 > getal2:
        return getal1
    elif getal2 > getal1:
        return getal2
    else:
        return getal1

c = grootste(12, 13)
print(c)