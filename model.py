
import math
import copy

PRAZNO = ' '
LADJICA = '#'
LADJICA_POTOPLJENA = '@'
NEZNANO = '?'

ERROR = 'error'
ZMAGA = 'zmaga'
KONEC_POSTAVLJANJA = 'konec_postavljanja'


class Ladjica():
    def __init__(self):
        self.polja = []
    


class Mreza():
    def __init__(self):
        self.velikost = 10
        self.mreza = [[PRAZNO for i in range(self.velikost)] for i in range(self.velikost)]
        self.poizkusi = [[False for i in range(self.velikost)] for i in range(self.velikost)]
        self.dolzine_ladjic = [0, 0, 1, 2, 1, 1] # stevilo ladjic posamezne dolžine, ki se jih lahko postavi

        self.ladjice = []
	
    def postavi_ladjico(self, dolzina, usmerjenost, y, x): 
        if self.dolzine_ladjic[dolzina] <= 0:
            return ERROR
        
        nova_ladjica = Ladjica()
        
        if usmerjenost == 'v':
            x = x
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
                if y_dol + 1  < self.velikost and self.mreza[y_dol + 1][x] == LADJICA:
                    veljavnost = False
                
                if veljavnost == False:
                    return ERROR
                else:
                    for i in range(y_gor, y_dol + 1):
                        self.mreza[i][x] = LADJICA
                        nova_ladjica.polja.append([i, x])
            else:
                return ERROR

        elif usmerjenost == 'h':
            y = y
            dolzina_levo = math.floor((dolzina - 1) / 2)
            dolzina_desno = math.ceil((dolzina - 1) / 2)
            if x - dolzina_levo >= 0 and x + dolzina_desno < self.velikost:
                x_levo = x - dolzina_levo
                x_desno= x + dolzina_desno

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
                if x_desno + 1  < self.velikost and self.mreza[y][x_desno + 1] == LADJICA:
                    veljavnost = False
                
                if veljavnost == False:
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
                if self.poizkusi[polje[0]][polje[1]] == False:
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
                if self.poizkusi[polje[0]][polje[1]] == False:
                    potopljena = False
                    break
            if potopljena:
                for polje in ladjica.polja:
                    mreza[polje[0]][polje[1]] = LADJICA_POTOPLJENA

        s = ''
        for y in range(len(self.mreza)):
            for x in range(len(self.mreza[y])):
                if self.poizkusi[y][x] == True:
                    s += mreza[y][x]
                else:
                    s += NEZNANO
            s += '\n'

        return s


    
    def __str__(self):
        s = ''
        for vrstica in self.mreza:
            for c in vrstica:
                s += c
            s += '\n'
        return s


m = Mreza()
print(m.postavi_ladjico(3, 'h', 5, 5))
print(m.postavi_ladjico(4, 'v', 1, 5))

m.streljaj(5, 5)
print(m.narisi_polje())
m.streljaj(5, 4)
print(m.narisi_polje())
m.streljaj(4, 5)
print(m.narisi_polje())
m.streljaj(5, 6)
print(m.narisi_polje())

print(m.ladjice[0].polja)
print(m.ladjice[1].polja)

'''
m.streljaj(0, 5)
m.streljaj(1, 5)
print(m.streljaj(2, 5))
print(m.streljaj(3, 5))

print(m.narisi_polje())

'''