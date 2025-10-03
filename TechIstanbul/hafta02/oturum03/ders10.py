# **kwargs kullanımı
def ogrenci_bilgisi(**bilgi):
    print(bilgi, type(bilgi))   # <class 'dict'>
    for anahtar, deger in bilgi.items():
        print(f"{anahtar} : {deger}")
    print("*******************")

ogrenci_bilgisi(ad="Berk",no="12",katilim=True,ortalama = 5.0)
ogrenci_bilgisi(ad="Tuğba",no="30",katilim=True,ortalama = 5.0)
ogrenci_bilgisi(ad="Rafa",no="27",katilim=False,ortalama = 2.2)

# **kwargs = keyword arguments
# *args = arguments

def urun_olustur(**kwargs):
    urun = {}
    for anahtar, deger in kwargs.items():
        urun[anahtar] = deger
    return urun

laptop = urun_olustur(urun_adi="asus",urun_fiyat = 15000, urun_stok=10)
print(laptop, type(laptop)) # <class 'dict'>

def ogrenciKarti(*args, **kwargs):
    print(args, type(args))
    print(kwargs, type(kwargs))
    for kart_bilgisi in args:
        print(kart_bilgisi)
        for bilgiler in kwargs:
            print(bilgiler, kwargs[bilgiler])

ogrenciKarti("Yök kartı", "Ulasim karti", o_adi= "Berk", o_soyadi ="AR", o_bolum = "Yazılım")

# fonksiyon (zorunlu_parametre, opsiyonel_parametre, *args, **kwargs)