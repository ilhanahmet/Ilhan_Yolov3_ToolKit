def buyut(ui):
    ui.resize(1000,600)

def kucult(ui):
    ui.resize(843, 420)

def buyumeKontrol(degiskenler,ui):
    if degiskenler.ekranBuyusunmu == True:
        buyut(ui)
        degiskenler.ekranBuyusunmu = False
    else:
        kucult(ui)
        degiskenler.ekranBuyusunmu = True


