class Futbolcu:
    kosu = "Koşabilir"
    depar = "Depar atar"
    maas = 500
    def __init__(self, ayak="sağ"):
        self.mevki = "Forvet"
        self.ayak = ayak

class Basketbolcu:
    turnike = "Turnike atabilir"
    ucluk = "Üçlük atabilir"
    maas = 750
    def __init__(self):
        self.bolge = "ileri"

class Multisporcu(Basketbolcu, Futbolcu):
    def __init__(self, ayak):
        Basketbolcu.__init__(self)
        Futbolcu.__init__(self, ayak)
    pass

berk = Futbolcu("Sağ")
print(vars(berk))   # {'mevki': 'Forvet', 'ayak': 'Sağ'}
print(berk.ayak)
print(berk.mevki)
print(berk.depar)
print(berk.kosu)
print(berk.maas)