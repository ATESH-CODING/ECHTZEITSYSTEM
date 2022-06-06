import random
import time



global wert_eins
global wert_zwei
iterativ = 10

def erzeugung_zwei():
    wert_zwei
    iterativ
    random.seed(time.time())
    for i in range(iterativ):
        wert_zwei += random.random()

    return wert_zwei

def erzeugung_eins():
    wert_eins
    iterativ
    random.seed(time.time())
    for i in range(iterativ):
        wert_eins += random.random()

    return wert_eins


print("hallo", erzeugung_eins(),erzeugung_zwei())