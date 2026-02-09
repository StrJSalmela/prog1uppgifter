korrektlösenord = "kod123"
while True:
    lösen = input("Fyll i lösenord:")
    if lösen==korrektlösenord:
        print("Välkommen!") 
        break
    
    else:
        print("Fel lösenord, försök igen!")