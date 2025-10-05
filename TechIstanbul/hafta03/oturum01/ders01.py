"""
ValueError int("abc") gibi geçersiz dönüşüm
IndexError liste[10] ama listede 5 eleman var
TypeError "merhaba" + 5 gibi uyumsuz işlem
KeyError sozluk["olmayan_anahtar"]
ZeroDivisionError 5 / 0 gibi sıfıra bölme
AttributeError nesne.yok_ozellik gibi var olmayan özellik erişimi
Exception tüm hataların üst sınıfı
NameError tanımlanmamış_değişken gibi tanımsız değişken erişimi
"""

"""
try:
    # riskli kodlar
    yas = int(input("Yaşınızı Giriniz: "))
    if yas < 18:
        print("Reşit değilsiniz.")
    else:
        print("Reşitsiniz")
except:
    # hata durumunda çalışacak kodlar
    print("Hata oluştu. Lüften geçerli bir yaş giriniz Sayısal veri olsun.")

print("Program sonlandı.")
"""


"""
try:
    sayi = int(input("Bir sayı giriniz: "))
    sayi2 = sayi / 0
except ValueError:
    print("Geçersiz giriş! Lütfen bir sayı giriniz.")
except Exception as e:
    print("Beklenmeyen bir hata oluştu: ", str(e))
"""

yas2 = int(input("Yaşınızı giriniz: "))

if yas2 < 0 or yas2 > 150:
    raise ValueError("Yaş 0 ile 150 arasında olmalı.")
else:
    print("Yaşınız: ",yas2)
    print("Geçerli yaş")