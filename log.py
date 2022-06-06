
try:
    with open('Messwerte.txt', 'w') as f:
        f.write('Create a new text file!')
        f.close()
except FileNotFoundError:
    print("File Exist")

with open('Messwerte.txt') as b:
    line = b.readline()
    print(line)
    b.close()