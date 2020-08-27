import bottle
import model


igra = model.Igra()

TIPI_POLJ = {
    model.NEZNANO: 'polje-neznano',
    model.PRAZNO: 'polje-prazno',
    model.LADJICA_POTOPLJENA: 'polje-ladjica-potopljena',
    model.LADJICA: 'polje-ladjica',
}

@bottle.get('/')
def zacetna_stran():
    return bottle.template('index.tpl')

@bottle.get('/zacni-igro')
def zacni_igro():
    igra.nova_igra()
    bottle.redirect('/igra')

@bottle.get('/igra')
def izris_polja():
    return bottle.template('igra.tpl',
                           tipi_polj=TIPI_POLJ,
                           mreza_igralec=igra.mreza_igralec.polja_1d(),
                           mreza_igralec_odkrita=igra.mreza_igralec.polja_1d_odkrito(),
                           mreza_racunalnik=igra.mreza_racunalnik.polja_1d(),
                           faza=igra.faza,
                           rezultat_poteze=igra.rezultat_poteze,
                           dolzine_ladjic=igra.mreza_igralec.dolzine_ladjic,
                           izbrana_dolzina=igra.izbrana_dolzina,
                           izbrana_usmerjenost=igra.izbrana_usmerjenost)

@bottle.post('/polje')
def klik_na_polje():
    i = int(bottle.request.forms.get('polje'))
    x = i % igra.mreza_igralec.velikost
    y = i // igra.mreza_igralec.velikost

    if igra.faza == model.POSTAVLJANJE:
        igra.izbrana_dolzina = int(bottle.request.forms.get('dolzina'))
        igra.izbrana_usmerjenost = bottle.request.forms.get('orinetacija')

    igra.klik_na_polje(y, x)

    bottle.redirect('/igra')

bottle.run()
