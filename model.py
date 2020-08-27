import math
import copy

import avtomatsko_igranje_bot

# tipi polja
PRAZNO = ' '
LADJICA = '#'
LADJICA_POTOPLJENA = '@'
NEZNANO = '?'

# sporocila funkcij
ERROR = 'error'
ZMAGA = 'zmaga'
PORAZ = 'poraz'
KONEC_POSTAVLJANJA = 'konec_postavljanja'

# faze igre
POSTAVLJANJE = 'postavljanje'
STRELJANJE = 'streljanje'
KONEC = 'konec'


class Ladjica():
    def __init__(self):
        self.polja = []


class Mreza():
    def __init__(self):
        self.velikost = 10
        self.mreza = [[PRAZNO for i in range(self.velikost)] for i in range(self.velikost)]
        self.poizkusi = [[False for i in range(self.velikost)] for i in range(self.velikost)]
        self.dolzine_ladjic = [0, 0, 1, 2, 1, 1]
        # stevilo ladjic posamezne dolzine, ki se jih lahko postavi

        self.ladjice = []

    def postavi_ladjico(self, dolzina, usmerjenost, y, x):
        if self.dolzine_ladjic[dolzina] <= 0:
            return ERROR

        nova_ladjica = Ladjica()

        if usmerjenost == 'v': # x za vsa polja enak
            dolzina_gor = math.floor((dolzina - 1) / 2)
            dolzina_dol = math.ceil((dolzina - 1) / 2)
            if y - dolzina_gor >= 0 and y + dolzina_dol < self.velikost:
                y_gor = y - dolzina_gor
                y_dol = y + dolzina_dol

                veljavnost = True

                for i in range(y_gor, y_dol + 1):
                    if self.mreza[i][x] == LADJICA:
                        veljavnost = False
                        break
                    if x - 1 >= 0 and self.mreza[i][x - 1] == LADJICA:
                        veljavnost = False
                        break
                    if x + 1 < self.velikost and self.mreza[i][x + 1] == LADJICA:
                        veljavnost = False
                        break
                if y_gor - 1 >= 0 and self.mreza[y_gor - 1][x] == LADJICA:
                    veljavnost = False
                if y_dol + 1 < self.velikost and self.mreza[y_dol + 1][x] == LADJICA:
                    veljavnost = False

                if not veljavnost:
                    return ERROR
                else:
                    for i in range(y_gor, y_dol + 1):
                        self.mreza[i][x] = LADJICA
                        nova_ladjica.polja.append([i, x])
            else:
                return ERROR

        elif usmerjenost == 'h': # y za vsa polja enak
            dolzina_levo = int(math.floor((dolzina - 1) / 2))
            dolzina_desno = int(math.ceil((dolzina - 1) / 2))
            if x - dolzina_levo >= 0 and x + dolzina_desno < self.velikost:
                x_levo = x - dolzina_levo
                x_desno = x + dolzina_desno

                veljavnost = True
                for i in range(x_levo, x_desno + 1):
                    if self.mreza[y][i] == LADJICA:
                        veljavnost = False
                        break
                    if y - 1 >= 0 and self.mreza[y - 1][i] == LADJICA:
                        veljavnost = False
                        break
                    if y + 1 < self.velikost and self.mreza[y + 1][i] == LADJICA:
                        veljavnost = False
                        break

                if x_levo - 1 >= 0 and self.mreza[y][x_levo - 1] == LADJICA:
                    veljavnost = False
                if x_desno + 1 < self.velikost and self.mreza[y][x_desno + 1] == LADJICA:
                    veljavnost = False

                if not veljavnost:
                    return ERROR
                else:
                    for i in range(x_levo, x_desno + 1):
                        self.mreza[y][i] = LADJICA
                        nova_ladjica.polja.append([y, i])
            else:
                return ERROR

        self.dolzine_ladjic[dolzina] -= 1
        self.ladjice.append(nova_ladjica)

        if sum(self.dolzine_ladjic) == 0:
            return KONEC_POSTAVLJANJA

    def streljaj(self, y, x):
        self.poizkusi[y][x] = True

        zmaga = True
        for ladjica in self.ladjice:
            potopljena = True
            for polje in ladjica.polja:
                if not self.poizkusi[polje[0]][polje[1]]:
                    potopljena = False
                    break

            if not potopljena:
                zmaga = False

        if zmaga:
            return ZMAGA
        else:
            return

    def narisi_polje(self):
        mreza = copy.deepcopy(self.mreza)

        for ladjica in self.ladjice:
            potopljena = True
            for polje in ladjica.polja:
                if not self.poizkusi[polje[0]][polje[1]]:
                    potopljena = False
                    break
            if potopljena:
                for polje in ladjica.polja:
                    mreza[polje[0]][polje[1]] = LADJICA_POTOPLJENA

        s = ''
        for y in range(len(self.mreza)):
            for x in range(len(self.mreza[y])):
                if self.poizkusi[y][x]:
                    s += mreza[y][x]
                else:
                    s += NEZNANO
            s += '\n'

        return s

    def polja_1d(self):
        izrisano = self.narisi_polje()
        tabela = []
        for vrstica in izrisano.split('\n')[:-1]:
            tabela.extend(list(vrstica))
        return tabela

    def polja_1d_odkrito(self):
        tabela = []
        for y in range(len(self.mreza)):
            for x in range(len(self.mreza[y])):
                tabela.append(self.mreza[y][x])
        return tabela

    def __str__(self):
        s = ''
        for vrstica in self.mreza:
            for c in vrstica:
                s += c
            s += '\n'
        return s


class Igra():
    def __init__(self):
        self.mreza_igralec = Mreza()
        self.mreza_racunalnik = Mreza()

        self.faza = POSTAVLJANJE
        self.izbrana_dolzina = 3
        self.izbrana_usmerjenost = 'v'
        self.rezultat_poteze = None

    def nova_igra(self):
        avtomatsko_igranje_bot.postavi_ladjice(self.mreza_racunalnik)

    def postavi_ladjico(self, dolzina, usmerjenost, y, x):
        rezultat = self.mreza_igralec.postavi_ladjico(dolzina, usmerjenost, y, x)
        if rezultat == KONEC_POSTAVLJANJA:
            self.faza = STRELJANJE
        return rezultat

    def streljaj(self, y, x):
        rezultat = self.mreza_racunalnik.streljaj(y, x)
        if rezultat == ZMAGA: # zmaga igralec
            self.faza = KONEC
            return ZMAGA

        p = avtomatsko_igranje_bot.naslednja_poteza(self.mreza_igralec)
        rezultat = self.mreza_igralec.streljaj(p[0], p[1])

        if rezultat == ZMAGA: # zmaga racunalnik
            self.faza = KONEC
            return PORAZ

    def klik_na_polje(self, y, x):
        if self.faza == POSTAVLJANJE:
            rezultat = self.postavi_ladjico(self.izbrana_dolzina, self.izbrana_usmerjenost, y, x)
            if rezultat == KONEC_POSTAVLJANJA:
                self.faza = STRELJANJE
            self.rezultat_poteze = rezultat
        elif self.faza == STRELJANJE:
            self.rezultat_poteze = self.streljaj(y, x)
