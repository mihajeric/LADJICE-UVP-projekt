import random

import model

from time import sleep

def naslednja_poteza(m):
    koordinate = [0, 0]

    izrisano = m.narisi_polje()

    tabela = []
    for vrstica in izrisano.split('\n')[:-1]:
        tabela.append(list(vrstica))

    for y in range(len(tabela)):
        vrstica = tabela[y]
        for x in range(len(vrstica)):
            znak = vrstica[x]
            if znak == model.LADJICA_POTOPLJENA:
                if y > 0 and tabela[y - 1][x] != model.LADJICA_POTOPLJENA:
                    tabela[y - 1][x] = model.PRAZNO
                if y < len(tabela) - 1 and tabela[y + 1][x] != model.LADJICA_POTOPLJENA:
                    tabela[y + 1][x] = model.PRAZNO
                if x > 0 and tabela[y][x - 1] != model.LADJICA_POTOPLJENA:
                    tabela[y][x - 1] = model.PRAZNO
                if x < len(vrstica) - 1 and tabela[y][x + 1] != model.LADJICA_POTOPLJENA:
                    tabela[y][x + 1] = model.PRAZNO
    
    potencialne_koordinate = []

    # iskanje še neznanih polj zraven nepotopljenih ladjic

    for y in range(len(tabela)):
        vrstica = tabela[y]
        for x in range(len(vrstica)):
            znak = vrstica[x]
            if znak == model.LADJICA:
                if y > 0 and tabela[y - 1][x] == model.NEZNANO:
                    potencialne_koordinate.append([y - 1, x])
                if y < len(tabela) - 1 and tabela[y + 1][x] == model.NEZNANO:
                    potencialne_koordinate.append([y + 1, x])
                if x > 0 and tabela[y][x - 1] == model.NEZNANO:
                    potencialne_koordinate.append([y, x - 1])
                if x < len(vrstica) - 1 and tabela[y][x + 1] == model.NEZNANO:
                    potencialne_koordinate.append([y, x + 1])
    

    if len(potencialne_koordinate) > 0:
        koordinate = random.choice(potencialne_koordinate)
    else:
        # naključno streljanje

        smiselna = False
        while not smiselna:
            y = random.randint(0, m.velikost - 1)
            x = random.randint(0, m.velikost - 1)
            if tabela[y][x] == model.NEZNANO:
                smiselna = True
        
        koordinate = [y, x]

    return koordinate


def postavi_ladjice(m):
    for dolzina in range(len(m.dolzine_ladjic) - 1, 0, -1):
        while m.dolzine_ladjic[dolzina] != 0:
            orientacija = random.choice(['v', 'h'])
            y = random.randint(0, m.velikost - 1)
            x = random.randint(0, m.velikost - 1)

            m.postavi_ladjico(dolzina, orientacija, y, x)

    return m



def main():
    m = model.Mreza()
    postavi_ladjice(m)
    print(m)
    sleep(1)
    
    zmaga = False
    i = 1
    while not zmaga:
        print(i)
        i += 1
        p = naslednja_poteza(m)
        zmaga = (m.streljaj(p[0], p[1]) == model.ZMAGA)
        print(m.narisi_polje())
        sleep(0.3)


if __name__ == '__main__':
    main()