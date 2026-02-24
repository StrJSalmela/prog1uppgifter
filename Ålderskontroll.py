try:
    ålder = int(input("Hur gammal är du? "))

    if ålder >= 18:
        print("Du är myndig!")

    else: 
        print("Du är omyndig!")
except ValueError: print("Använd heltal vid inmatning, prova igen!")