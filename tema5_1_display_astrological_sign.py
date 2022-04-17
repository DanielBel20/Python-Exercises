"""Write a Python program to display astrological sign for given date of birth
Expected Output:
Input birthday: 15
Input month of birth (e.g. march, july etc): may
Your Astrological sign is : Taurus

Berbec: 21 martie - 20 aprilie
Taur: 21 aprilie - 21 mai
Gemeni: 22 mai - 21 iunie
Rac: 22 iunie - 22 iulie
Leu: 23 iulie - 22 august
Fecioară: 23 august - 22 septembrie
Balanță: 23 septembrie - 22 octombrie
Scorpion: 23 octombrie - 21 noiembrie
Săgetator: 22 noiembrie - 21 decembrie
Capricorn: 22 decembrie - 20 ianuarie
Vărsător: 21 ianuarie - 18 februarie
Pești: 19 februarie - 20 martie"""

month = input("Enter your month of birth: ")
birthday = int(input("Enter your birthday: "))

if month.lower() == "march":
    if birthday in range(21, 32):
        print("Zodia ta este: Berbec")
    elif birthday in range(1, 21):
        print("Zodia ta este: Pesti")
    else:
        print("Nu ai introdus ziua corecta!")
if month.lower() == "april":
    if birthday in range(21, 31):
        print("Zodia ta este: Taur")
    elif birthday in range(1, 21):
        print("Zodia ta este: Berbec")
    else:
        print("Nu ai introdus ziua corecta!")
if month.lower() == "may":
    if birthday in range(22, 32):
        print("Zodia ta este: Gemeni")
    elif birthday in range(1, 22):
        print("Zodia ta este: Taur")
    else:
        print("Nu ai introdus ziua corecta!")
if month.lower() == "june":
    if birthday in range(22, 31):
        print("Zodia ta este: Rac")
    elif birthday in range(1, 22):
        print("Zodia ta este: Gemeni")
    else:
        print("Nu ai introdus ziua corecta!")
if month.lower() == "july":
    if birthday in range(23, 32):
        print("Zodia ta este: Leu")
    elif birthday in range(1, 23):
        print("Zodia ta este: Rac")
    else:
        print("Nu ai introdus ziua corecta!")
if month.lower() == "august":
    if birthday in range(23, 32):
        print("Zodia ta este: Fecioara")
    elif birthday in range(1, 23):
        print("Zodia ta este: Leu")
    else:
        print("Nu ai introdus ziua corecta!")
if month.lower() == "september":
    if birthday in range(23, 31):
        print("Zodia ta este: Balanta")
    elif birthday in range(1, 23):
        print("Zodia ta este: Fecioara")
    else:
        print("Nu ai introdus ziua corecta!")
if month.lower() == "october":
    if birthday in range(23, 32):
        print("Zodia ta este: Scorpion")
    elif birthday in range(1, 23):
        print("Zodia ta este: Balanta")
    else:
        print("Nu ai introdus ziua corecta!")
if month.lower() == "november":
    if birthday in range(22, 31):
        print("Zodia ta este: Sagetator")
    elif birthday in range(1, 22):
        print("Zodia ta este: Scorpion")
    else:
        print("Nu ai introdus ziua corecta!")
if month.lower() == "december":
    if birthday in range(22, 32):
        print("Zodia ta este: Capricorn")
    elif birthday in range(1, 22):
        print("Zodia ta este: Sagetator")
    else:
        print("Nu ai introdus ziua corecta!")
if month.lower() == "january":
    if birthday in range(21, 32):
        print("Zodia ta este: Varsator")
    elif birthday in range(1, 21):
        print("Zodia ta este: Capricorn")
    else:
        print("Nu ai introdus ziua corecta!")
if month.lower() == "february":
    if birthday in range(19, 30):
        print("Zodia ta este: Pesti")
    elif birthday in range(1, 19):
        print("Zodia ta este: Varsator")
    else:
        print("Nu ai introdus ziua corecta!")
