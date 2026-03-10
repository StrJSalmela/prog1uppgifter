while True:
    print("\nKalkylator") 
    print("1. Addera")
    print("2. Subtrahera")
    print("3. Multiplicera")
    print("4. Avsluta")

    val = input("Välj ett alternativ: ")

    if val == "1":
        tal1 = int(input("Skriv ett tal: "))
        tal2 = int(input("Skriv ett till tal: "))
        print("Summan är ",tal1 + tal2)
        
    elif val == "2": 
        tal1 = int(input("Skriv ett tal: "))
        tal2 = int(input("Skriv ett till tal: "))
        print("Summan är ",tal1 - tal2)


    elif val == "3":
        tal1 = int(input("Skriv ett tal: "))
        tal2 = int(input("Skriv ett till tal: "))
        print("Summan är ",tal1 * tal2)

    elif val == "4":
        print("Programmet avslutas")
        break

    else:
        print("\nOgiltigt, var vänlig försök igen")