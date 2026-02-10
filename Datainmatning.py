summa = 0

while summa < 100:
    tal = int(input("Mata in ett tal: "))
    summa += tal
    print("Nuvarande summa:", summa)
if summa >= 100: 
    print("Du har nått gränsen!")