try:
    tal = int(input("Mata in ett heltal: ")) # Ber användaren mata in ett heltal
    print("Du skrev:", tal) # Mening som printas ut om inmatningen var ett heltal
except ValueError: # Felhantering
    print("Fel! Inmatning behöver vara ett heltal.") # Mening som printas vid felaktig datatyp