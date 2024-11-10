broj_redova = 2
broj_praznih = 0
broj = 1


while(broj_redova % 2 == 0):
    broj_redova = int(input())

for i in range(broj_redova):

    red = ""

    if i < (broj_redova - 1) / 2:
        for a in range(((broj_redova-1)//2)-broj_praznih):
            red += " "
        for b in range(broj):
            red += "*"
        for c in range(((broj_redova-1)//2)-broj_praznih):
            red += " "

        broj += 2
        broj_praznih += 1
        print(red)



    elif i == (broj_redova - 1) / 2:
        for d in range(broj_redova):
            red += "*"
        print(red)
        broj -= 2
        broj_praznih -= 1

    else:
        for e in range(((broj_redova-1)//2)-broj_praznih):
            red += " "
        for f in range(broj):
            red += "*"
        for g in range(((broj_redova-1)//2)-broj_praznih):
            red += " "

        broj -= 2
        broj_praznih -= 1
        print(red)
