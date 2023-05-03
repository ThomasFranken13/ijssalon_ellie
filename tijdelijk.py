from helper import decoreer

def print_aanbieding():
    prijzen = {
        "Aardbei" : 3,
        "Vanille" : 4,
        "Chocolade" : 5
    }

    aanbieding = prijzen["Vanille"] * 0.8
    
    reclame_tekst = f"Vandaag in de aanbieding: Vanille-ijs, 1 liter - slechts € {aanbieding}"
    
    reclame_tekst2 = reclame_tekst[:63]
    
    reclame_tekst3 = reclame_tekst2 .upper()
    
    reclame_tekst4 = reclame_tekst3 .split()
    
    for el in reclame_tekst4:
        if len(el) >= 5:
            print(el .upper())
        elif len(el) <= 4:
            print(el .lower())
            
print_aanbieding()

decoreer("aanbieding")
