# Skapa en lista med tal
numbers = [10, 20, 30, 40, 50] #hakparentes saknades, listan blev inte stängd (syntaxfel)

# Räkna ut summan av talen
total = 0
for num in numbers: #kolon saknades (syntaxfel)
    total = total + num

# Beräkna medelvärdet
average = total / len(numbers) #felstavad variabel, numberss ska vara numbers (körtidsfel)

# Skriv ut resultatet
print("Medelvärdet är: ", average) #Python kan inte konkatenera str & float, ändrar "+" till "," (körtidsfel)