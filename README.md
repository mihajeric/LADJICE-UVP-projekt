# Ladjice
## Zagon programa
Zagnati je treba datoteko `ladjice.py` s Python 3, preko terminala v direktoriju projekta npr. z `python3 ladjice.py` oz. `python ladjice.py` (odvisno od instalacije pythona). 
S tem se zažene server, v terminalu se izpiše URL naslov, na katerem je dostopen spletni vmesnik (default http://127.0.0.1:8080/). 

## Navodila za igranje
Najprej je treba postaviti ladjice (1×dolžine 2, 2×3, 1×4, 1×5). V zgornjem meniju se izbere dolžino in orientacijo (vertikalno/horizontalno), potem pa se klikne na polje, kjer naj bo sredina novopostavljene ladjice. Ko so postavljene že vse, program avtomatsko preusmeri na začetek igre.  

S klikom na polje v desni mreži se strelja na nasprotnikovo (računalnikovo) mrežo, kjer so bile ladjice naključno postavljene. Po vsaki potezi bo potezo naredil še računalnik, ki cilja na tvoje polje. Kaj računalnik vidi je vidno na levi mreži. Zmaga tisti, ki prvi zadane vse nasprotnikove ladjice.

### Legenda tipov polj
- Sivo: še neodkrito polje
- Modro: polje brez ladjice
- Oranžno: polje z zadeto, a še nepotopljeno ladjico
- Rdeče: potopljena ladjica