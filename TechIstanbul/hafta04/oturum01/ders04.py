# kitap = {"ad": "", "yazar": ""}

class Kitap:
    ad = ""
    yazar = ""
    sayfaSayisi = 0
    basimYili = 0
    yayinEvi = ""

kitap1 = Kitap()
kitap1.ad = "Hayvan Çiftliği"
kitap1.yazar = "George Orwell"
kitap1.sayfaSayisi = 80
kitap1.yayinEvi = "Techistanbul"
kitap1.basimYili = 1950

print(kitap1.ad) # Hayvan Çiftliği

degiskenler = vars(kitap1)
print(degiskenler)  # {'ad': 'Hayvan Çiftliği', 'yazar': 'George Orwell', 'sayfaSayisi': 80, 'yayinEvi': 'Techistanbul', 'basimYili': 1950}