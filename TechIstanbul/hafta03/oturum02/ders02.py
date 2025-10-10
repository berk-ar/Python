import math # matematik kütüphanesi
import random
import datetime

print(help(math.pow))

print("----Matematik Modülü----")
print("Pi sayısı", math.pi) # Pi sayısı 3.141592653589793
print("2 sayısının 3 kuvveti", math.pow(2,3))   # 2 sayısının 3 kuvveti 8.0
print("Karekök 16 = ", math.sqrt(16))   # Karekök 16 =  4.0
print("Yuvarlama: ", round(4.7))    # Yuvarlama:  5
print("Yuvarlama: ", round(4.4))    # Yuvarlama:  4

# Random modülü
print("----Random Modülü----")
print("0-1 aralığında sayı üret : ", random.random())
print("0-100 aralığında tam sayı üret: ", random.randrange(0,100))
print("0-100 aralığında tam sayı üret: ", random.randrange(0,100))
print("1.0-5.0 aralığında tam sayı üret: ", random.uniform(1.0,5.0))

renkler = ["siyah","beyaz","mavi"]
secilenRenk = random.choice(renkler)    # liste içerisinden rastgele bir seçim yapar
print(secilenRenk)

random.shuffle(renkler) # renkler listesindeki elemanları karıştırır
print(renkler)
print(type(renkler))    # <class 'list'>

# Datetime tarih ve saat işlemleri için kullanılır
print("----Datetime----")
simdi = datetime.datetime.now()
print("Şimdi: ",simdi)    # 2025-10-10 12:06:52.732430
print("Yıl: ", simdi.year)
print("Ay: ", simdi.month)
print("Gün: ", simdi.day)
print("Saat: ", simdi.hour)
print("Dakika: ", simdi.minute)
print("Saniye: ", simdi.second)
print("Gün: ", simdi.__class__) # <class 'datetime.datetime'>
print("Haftanın kaçıncı günü:", simdi.strftime("%w"))
print("Haftanın hangi günü:", simdi.strftime("%A"))
print("Tarih Formatı:",simdi.strftime("%d/%m/%Y"))
print("Saat Formatı:",simdi.strftime("%H:%M:%S"))