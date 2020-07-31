import random

import model

def naslednja_poteza(m):
    koordinate = [0, 0]

    izrisano = m.narisi_polje()


    # naključno streljanje

    smiselna = False
    while not smiselna:
        y = random.randint(0, m.velikost - 1)
        x = random.randint(0, m.velikost - 1)
        if m.poizkusi[y][x] == False:
            smiselna = True
    
    koordinate = [y, x]

    return koordinate



def main():
    for i in range(95):
        p = naslednja_poteza(model.m)
        model.m.streljaj(p[0], p[1])
        print(model.m.narisi_polje())


if __name__ == '__main__':
    main()