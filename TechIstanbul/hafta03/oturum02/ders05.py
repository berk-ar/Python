# Doğum gününe kalan gün hesaplama

from datetime import datetime

dogum = input("Doğum tarihini giriniz (GG.AA.YYYY) : ")
gun, ay, yil = map(int, dogum.split("."))
print(gun, ay, yil)
dtDogum = datetime(yil, ay, gun)
print(dtDogum)
bugun = datetime.now()
print("Bugün",bugun)
buYilDogum = dtDogum.replace(year=bugun.year)
print("Bu Yıl ki doğum günü", buYilDogum)

if buYilDogum < bugun:
    print((bugun - buYilDogum).days,"ün önce doğum gününüzdü")
    buYilDogum = buYilDogum.replace(year = bugun.year + 1)

kalan = (buYilDogum - bugun).days
print("Doğum gününüze kalan gün sayısı", kalan)