import bottle
import model
import avtomatsko_igranje_bot


igra = model.Igra()

tipi_polj = {
    model.NEZNANO: 'polje-neznano',
    model.PRAZNO: 'polje-prazno',
    model.LADJICA_POTOPLJENA: 'polje-ladjica-potopljena',
    model.LADJICA: 'polje-ladjica',
}

@bottle.get("/")
def zacetna_stran():
    return bottle.template("index.tpl")

@bottle.get("/zacni-igro")
def zacni_igro():
    igra.nova_igra()
    bottle.redirect("/igra")
    

@bottle.get("/igra")
def izris_polja():
    p = avtomatsko_igranje_bot.naslednja_poteza(igra.mreza_racunalnik)
    print(p)
    igra.streljaj(p[0], p[1])

    return bottle.template("igra.tpl", tipi_polj=tipi_polj, mreza_igralec=igra.mreza_igralec.polja_1d(), mreza_racunalnik=igra.mreza_racunalnik.polja_1d())

bottle.run()