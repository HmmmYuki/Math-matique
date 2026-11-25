from random import randint
for i in range(100):
    r = randint (0, 1)
    if r <= 0.1252:
        de = 1
    elif r <= 0.1309:
        de = 2
    elif r <= 0.2157:
        de = 3
    elif r <= 0.1987:
        de = 4
    elif r <= 0.1123:
        de = 5
    elif r <= 0.2172:
        de = 6

print (de)