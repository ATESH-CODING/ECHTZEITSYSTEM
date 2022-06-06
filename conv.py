import random


iterativ = 10

def erzeuge_wert():
    global iterativ
    wert = 0
    for i in range(iterativ):
        wert += random.randint(0,iterativ)

    return wert

def liste():

    liste = [0]

    for i in range(iterativ):
        temp = erzeuge_wert()

        if temp > i:
            liste.append(temp)


    return liste;

print(liste())