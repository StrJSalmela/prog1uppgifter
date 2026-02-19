korrektlösenord = "kod123" # Variabel för korrekt lösenord

while True: # While-loop körs tills användaren matar in korrekt lösenord
    lösen = input("Fyll i lösenord:") # Lösenordsinmatning från användare
    if lösen == korrektlösenord: # Kontrollera input mot korrekta lösenordet
        print("Välkommen!") # Print för korrekt lösenord
        break # While-loopens stop om inmatat lösenord stämmer med korrekta lösenordet
    
    else: # Ifall if-villkor inte uppfylls
        print("Fel lösenord, försök igen!") # Skriv ut felmeddelande och be användaren försöka igen

# Det finns ingen felhantering i koden, råkar man ändra variabeln för lösenord, utan att ändra if-satsens variabel, så fungerar inte programmet
# Användaren kan inte logga in trots rätt lösenord, och kanske inte förstår felmeddelandet
# I koden finns inget max-antal försök för att mata in lösenord. Det gör användares inloggning sårbar för obehöriga