def permutacije(array, number=0, number1=0):
    if  number == len(array):
        print(*array)
    else:
        for i in range(number, len(array)):
            number1 = array[number]
            array[number] = array[i]
            array[i] = number1
            permutacije(array, number + 1)
            number1 = array[number]
            array[number] = array[i]
            array[i] = number1

unos = input("Unesite niz cijelih brojeva: ")

array = list(map(int, unos.split()))


permutacije(array)
