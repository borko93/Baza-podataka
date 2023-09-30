def baza_podataka():

    def licni_podaci():  # lični podaci koji uključuju:ime, prezime, pol,...
        ime = input("Kako se zovete?\n")
        prezime = input("Kako se prezivate?\n")
        pol = int(input("Kojeg ste pola?\n1-Muški\n2-Ženski\n"))
        if pol == 2:
            djevojacko_prezime = input("Vaše djevojačko prezime:\n")
        godina_rodjenja = int(input("Koje godine ste rođeni?\n"))
        print("")
        print("Svi vaši podaci će ostati anonimni")
        pristanak = int(
            input("Pristajete li da ih pohranimo u našu bazu?\n1-Da\n2-Ne\n"))

        if pristanak == 1:
            print(ime,  djevojacko_prezime, prezime,
                  "drago nam je da vjerujete našoj politici privatnosti vaših podataka!\n Ovom opcijom ste potvrdili da želite da nastavite sa unosom podataka u našu bazu.\n")
            print("")
            input("Pritisnite ENTER da nastavite")
            print("")
            licni_podaci_2()
        elif pristanak == 2:
            print("Cijenimo Vašu obzirnost prema sopstvenoj sigurnosti, ali uvjeravamo Vas da našu bazu podataka koriste naši odabrani klijenti iz cijelog svijeta")
            print("")
            pristanak_2 = int(
                input("Da li zaista želite da odustanete?\n1-Da\n2-Ne"))
            if pristanak_2 == 1:
                input("Pritisnite ENTER da izađete")
                quit()
            elif pristanak_2 == 2:
                input("Da pređete na sljedeću fazu unosa podataka, pritisnite ENTER\n")
                licni_podaci_2()

    def licni_podaci_2():
        godina_upisa_na_fakultet = int(
            input("Unesite Vašu godinu upisa na fakultet\n"))
        print("")
        prosjek_ocjena = float(
            input("Koja je prosječna ocjena kojom ste završili osnovne studije?\n"))
        print("")
        print("Da li ste zadovoljni Vašim prosjekom?\n1-Da\n2-Ne\n3-Ne znam\n")
        odgovor_prosjek = int(input(""))
        if odgovor_prosjek == 1:
            print(
                "Vi ste zaista srećna osoba, samo nastavite da širite pozitivnu energiju\n")
            print("")
            input("Pritisnite ENTER da nastavite dalje")
            podaci_o_braku()
        elif odgovor_prosjek == 2:
            print("Imate pravo na svoje mišljenje\n")
        elif odgovor_prosjek == 3:
            print("Morate da budete odlučniji\n")

    def header():

        line01 = ("***************************************************")
        line02 = ("***************************************************")
        line03 = ("****😊 Dobrodošli u sistem za unos podataka 😊****")
        line00 = (" ")

        print("")
        print(line01)
        print(line02)
        print(line00)
        print(line03)
        print(line00)
        print(line01)
        print(line01)
        print(line00)
        print(line00)
        input("Pritisnite bilo koje dugme da započnete...\n")

    def podaci_o_braku():
        bracno_stanje = int(input(
            "Unesite vaše bračno stanje:\n1-Oženjen/udata\n2-Neoženjen/neudata\n3-Razveden/razvedena\n4-Ne bih se izjasnio/la\n"))
        if bracno_stanje == 1:
            mjeseci_u_braku = int(input("Koliko mjeseci ste u braku?\n"))
            godina_upoznavanja = int(
                input("Koje godine ste se upoznali sa vašim mužem/ženom?\n"))
            borkovo_godiste = int(input("Koje godište je Vaš muž/žena?\n"))
            print("")
            input("Pritisnite ENTER da pređemo u sljedeću podsekciju podataka o braku")
            skala_ljubavi()
            rsp()
            rsp()
            rsp()
            print("")
            input("Da bi ste započeli analizu do sad unijetih podataka pritisnite ENTER")

        elif bracno_stanje == 2:
            print("Nadam se da ćete naći vašu srodnu dušu.\n")
            input("Pritisnite ENTER da zaigrate našu igru\n")
            rsp()
        elif bracno_stanje == 3:
            godina_razvoda = int(input("Koje godine ste se razveli?\n"))
            razvod_izbor = input(
                "Za Vas je ovdje kraj puta, pritisnite:\n1-Da izađete iz programa\n2-Da igrate našu igru <PAPIR, KAMEN, MAKAZE>")
            if razvod_izbor == 1:
                quit()
            elif razvod_izbor == 2:
                rsp()
        elif bracno_stanje == 4:
            print(
                "Morate biti odlučniji, pritisnite ENTER da zaigrate našu igru <KAMEN, PAPIR, MAKAZE>")
            input()
            rsp()

    def skala_ljubavi():
        skala = int(input("Koliko na skali od 1 do 10 volite vašeg muža?\n"))

        input("Ukoliko želite da zaigrate našu igru, pritisnite ENTER")

    def rsp():
        import sys
        import random
        from enum import Enum

        class RPS(Enum):
            PAPIR = 1
            MAKAZE = 2
            DIJAMANT = 3

        playagain = True

        while playagain:

            izbor = input(
                "\nUnesite broj...\n1 za papir\n2 za makaze ili\n3 za dijamant\n\n")

            igrač = int(izbor)

            if igrač < 1 or igrač > 3:
                sys.exit("Morate unijete brojeve: 1, 2 ili 3.")

            izbor_kompjutera = random.choice("123")
            kompjuter = int(izbor_kompjutera)
            print("\nVi ste izabrali " +
                  str(RPS(igrač)).replace('RPS.', '') + ".")
            print("Kompjuter je izabrao " +
                  str(RPS(kompjuter)).replace('RPS.', '') + ".\n")

            if igrač == 1 and kompjuter == 3:
                print("Pobijedili ste.\n")
            elif igrač == 2 and kompjuter == 1:
                print("🥳 Pobijedili ste.\n")
            elif igrač == 3 and kompjuter == 2:
                print("🥳 Pobijedili ste.\n")
            elif igrač == kompjuter:
                print("😒 Neriješeno. Igrajte ponovo.\n")
            else:
                print("💻 Kompjuter je pobijedio.\n")

            playagain = input("\nNova igra?\nY za da ili\nQ da izađete \n\n")

            if playagain.lower() == "y":
                continue
            else:
                print("\n🥳🥳🥳")
                print("Hvala što ste igrali!")
                playagain = False
        sys.exit("Doviđenja!")

    header()

    licni_podaci()

    podaci_o_braku()

    skala_ljubavi()

    rsp()

    print("")
    input("Igra je završena\nDa bi ste izašli iz programa pritisnite ENTER")

    quit()


baza_podataka()
