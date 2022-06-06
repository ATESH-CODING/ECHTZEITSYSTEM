
try:
    liste = [1,2,3,4,5,6,6]

    with open('Messwerte.txt', 'w') as f:
        f.write(' '. join(str(e) for e in liste))
        f.close()
except FileNotFoundError:
    print("File Exist")

with open('Messwerte.txt') as b:
    line = b.readline()
    print(line)
    b.close()