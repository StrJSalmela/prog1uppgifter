Kontaktlista = {}

while True:
    print("\nKontaktbok")
    print("1. Lägg till kontakt")
    print("2. Sök efter kontakt")
    print("3. Avsluta")

    val = input("Välj ett av alternativen: ")

    if val == "1":
        namn = input("Ange namn: ")
        nummer = input("Ange nummer: ")
        Kontaktlista[namn] = nummer
        print(namn, "tillagd.")
    
    elif val == "2":
        namn = input("Vem vill du söka efter? ")
        if namn in Kontaktlista:
            print(namn, "-", Kontaktlista[namn])
        else:
            print("Kontakten finns inte i din kontaktbok, var vänlig försök igen!")

    elif val == "3":
        print("Programmet avslutas")
        break

    else:
        print("Ogiltigt val, försök igen")