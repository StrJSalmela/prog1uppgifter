användarnamn = set()

while True:

    namn = input("Skriv ett användarnamn (eller skriv avsluta): ")
    if namn in användarnamn:
        print("Användarnamnet finns redan")
    elif namn == "avsluta":
        print("Tillagda användarnamn: " ,användarnamn)
        break
    else:
        print("Användarnamnet tillagt")
        användarnamn.add(namn)