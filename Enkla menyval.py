import datetime # Importerar datetimepaketet för att få aktuellt datum i val 1

while True:
    print("\n Hej och välkommen hit") #\n för snyggare utskrift i terminalen, och hälsar användare välkommen
    print("Gör ett av följande val:")
    print("Skriv 1 för att se dagens datum")
    print("Skriv 2 för att avsluta programmet")

    val = input("Välj ett av alternativen: ") # Hämtar data från användare

    if val == "1": # Val 2 skriver ut dagens datum
        dagens_datum = datetime.date.today()
        print("\nDagens datum är:" , dagens_datum)
    elif val == "2": # Val 2 avslutar programmet
        print("\nProgrammet avslutas, tack och hejdå!")
        break
    else:
        print("\nOgiltigt, var vänlig försök igen") # Fångar upp ogiltigt val