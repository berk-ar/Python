# parametreli ve geriye değer döndürmeyen fonksiyonlar
def selamla(isim):
    print(f"Merhaba {isim}, Python bootcampe hoşgeldiniz.")

selamla("Berk")
selamla("Tuğba")
print(type(selamla))    # <class 'function'>

def toplama(a,b):
    sonuc = a + b
    print(f"{a} + {b} = {sonuc}")

toplama(1,2)
toplama(10,3)

x = toplama(7,8)
print(x)    # None