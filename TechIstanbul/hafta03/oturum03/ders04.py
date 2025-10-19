# Dosyadan veri okuma
with open("kayit.txt", "r") as dosya:
    print(dosya.readline())
    print(dosya.readline())

print("-------------------------------")

with open("kayit.txt", "r") as dosya:
    for x in dosya:
        print(x)

print("-------------------------------")

dosya = open("kayit.txt", "r")
metin = dosya.read()
print(metin)