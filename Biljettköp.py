biljett = input("Vill du köpa biljett för vuxen, pensionär eller barn? ")

if biljett == "vuxen": 
    pris = 50
elif biljett == "pensionär":
    pris = 30
elif biljett == "barn":
    pris = 20
else:
    pris = None

if pris is not None:
    print("Kvitto för ditt köp")
    print("Biljetttyp:",biljett, ", pris:",pris, " kronor, välkommen åter!")
else:
    print("Ogiltig biljettyp, vänligen försök igen")
    