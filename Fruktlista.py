fruktlistan = ["mango", "päron", "banan"]

while True:
    print("\nMeny:")
    print("1. Visa fruktlista:")
    print("2. Lägg till frukt:")
    print("3. Ta bort frukt")
    print("4. Avsluta programmet")

    val = input("Välj ett alternativ:")

    if val == "1":
        print(fruktlistan)
    
    elif val == "2":
        frukt_tillägg = input("Vilken frukt vill du lägga till?")
        fruktlistan.append(frukt_tillägg)
        print("Uppdaterad version av fruktlistan: ", fruktlistan)
    
    elif val == "3":
        borttagen_frukt = input("Vilken frukt vill du ta bort?")
        if borttagen_frukt in fruktlistan:
            fruktlistan.remove(borttagen_frukt)
            print("Du har tagit bort ", borttagen_frukt)
            print("Uppdaterad version av fruktlistan: ", fruktlistan)
        else:
            print("Fel: Frukten finns inte i listan")
    
    elif val == "4":
        print("Programmet avslutas, tack och hej!")
        break
    
    else:
        print("Ogiltigt val, försök igen")