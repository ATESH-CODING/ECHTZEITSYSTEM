import random
import time




iterativ = 10

def erzeugung_zwei():
    global iterativ
    wert_zwei = 0
    for i in range(iterativ):
        wert_zwei += random.randint(0,10)

    return wert_zwei

def erzeugung_eins():
    global iterativ
    wert_eins = 0
    for i in range(iterativ):
        wert_eins += random.randint(0,10)

    return wert_eins

def pruefe_werte():

    schleife = True

    while schleife:
        eins = erzeugung_eins()
        zwei = erzeugung_zwei()
        if (eins != zwei) and (eins <= zwei):
            schleife = False

    if not schleife:
        return eins,zwei


eins, zwei = pruefe_werte()
print(eins,zwei)