polja = [1,2,3,4,5,6,7,8,9]
polja_prvog_igraca = []
polja_drugog_igraca = []
niz = []
index = 0
broj = 0

def printanje_matrice(niz):
    g = 0
    niz = []
    for k in range(3):

        for j in range(3):
            niz.append(polja[g])
            g += 1

        print(niz)
        niz = []

def pobjeda_prvog(broj):
    polja_prvog_igraca.sort()
    if polja_prvog_igraca == [1,2,3] or polja_prvog_igraca == [4,5,6] or polja_prvog_igraca == [7,8,9] or polja_prvog_igraca == [1,4,7] or polja_prvog_igraca == [2,5,8] or polja_prvog_igraca == [3,6,9] or polja_prvog_igraca == [1,5,9] or polja_prvog_igraca == [3,7,5]:
        print("Igrac broj 1 je pobijedio")
        broj = 1

def pobjeda_drugog(broj):
    polja_drugog_igraca.sort()
    if polja_drugog_igraca == [1,2,3] or polja_drugog_igraca == [4,5,6] or polja_drugog_igraca == [7,8,9] or polja_drugog_igraca == [1,4,7] or polja_drugog_igraca == [2,5,8] or polja_drugog_igraca == [3,6,9] or polja_drugog_igraca == [1,5,9] or polja_drugog_igraca == [3,7,5]:
        print("Igrac broj 2 je pobijedio")
        broj = 1

for i in range(9):

    if i == 0 or i % 2 == 0:
        odabrano_polje = int(input())
        if odabrano_polje >= 1 and odabrano_polje <= 9:
            if odabrano_polje in polja:

                polja_prvog_igraca.append(odabrano_polje)
                index = polja.index(odabrano_polje)
                polja[index] = "X"

                pobjeda_prvog(broj)
                printanje_matrice(niz)

                if broj == 1:
                    break

            else:
                print("Polje je već odigrano")
                i -= 1
        else:
            print("Broj se ne nalazi u intervalu od 1 do 9")
            i -= 1

    else:
        odabrano_polje = int(input())
        if odabrano_polje >= 1 and odabrano_polje <= 9:
            if odabrano_polje in polja:

                polja_drugog_igraca.append(odabrano_polje)
                index = polja.index(odabrano_polje)
                polja[index] = "O"

                pobjeda_drugog(broj)
                printanje_matrice(niz)
                
                if broj == 1:
                    break

            else:
                print("Polje je već odigrano")
                i -= 1
        else:
            print("Broj se ne nalazi u intervalu od 1 do 9")
            i -= 1

if broj == 0:
    print("Igra je ostala neriješna")