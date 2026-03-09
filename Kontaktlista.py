Kontaktlista = {}

while True:
    print("\nKontaktlista")
    print("1. lägg till kontakt")
    print("2. sök efter kontakt")
    print("3. ta bort kontakt")
    print("4. Avsluta")

    val = input("välj ett av alternativen: ")

    if val == "1":
        namn = input("Ange namn: ")
        nummer = input("Ange nummer: ")
        Kontaktlista[namn] = nummer
        print("Kontakten tillagd.")
    
    elif val == "2":
        namn = input("Vem vill du söka efter? ")
        if namn in Kontaktlista:
            print(namn, "-", Kontaktlista[namn])
        else:
            print("ingen kontakt med det namnet finns i kontaktlistan")
    
    elif val == "3":
        namn = input("Vem vill du ta bort? ")
        if namn in Kontaktlista:
            del Kontaktlista[namn]
            print("Kontakten borttagen")
        else:
            print("Ingen sådan kontakt finns i kontaktlistan")
    
    elif val == "4":
        print("Programmet avslutas")
        break

    else:
        print("Ogiltigt val, försök igen")