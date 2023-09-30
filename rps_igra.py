def igra():

    import sys
    import random
    from enum import Enum

    class RPS(Enum):
        PAPIR = 1
        MAKAZE = 2
        DIJAMANT = 3

    print(" ")

    izbor = input(
        "Unesite broj...\n1 za papir\n2 za makaze ili\n3 za dijamant\n\n")

    igrač = int(izbor)

    if igrač < 1 or igrač > 3:
        sys.exit("Morate unijete brojeve: 1, 2 ili 3.")

    izbor_kompjutera = random.choice("123")
    kompjuter = int(izbor_kompjutera)
    print("")
    print("Vi ste izabrali " + str(RPS(igrač)).replace('RPS.', '') + ".")
    print("Kompjuter je izabrao " + str(RPS(kompjuter)).replace('RPS.', '') + ".")
    print("")

    if igrač == 1 and kompjuter == 3:
        print("Pobijedili ste.")
    elif igrač == 2 and kompjuter == 1:
        print("🥳 Pobijedili ste.")
    elif igrač == 3 and kompjuter == 2:
        print("🥳 Pobijedili ste.")
    elif igrač == kompjuter:
        print("😒 Neriješeno. Igrajte ponovo.")
    else:
        print("💻 Kompjuter je pobijedio.")

    print("")
