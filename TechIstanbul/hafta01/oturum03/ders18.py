# sayı tahmin oyunu
import random

tutulan = random.randint(1,10)

print("1-10 aralığında bir sayı tahmin edin.")

while True:
    tahmin = int(input("Tahminini yaz: "))
    if tahmin < 1 or tahmin > 10:
        print("Sayıyı 1-10 arasında girmelisiniz.")
        continue
    elif tahmin == tutulan:
        print("Tebrikler, bildiniz.")
        break
    elif tahmin > tutulan:
        print("Daha küçük bir değer giriniz.")
    elif tahmin < tutulan:
        print("Daha büyük bir değer giriniz.")