# Dosyadan veri okuma
# dosya = open("denemeKayit.txt", "r") # => FileNotFoundError: [Errno 2] No such file or directory: 'denemeKayit.txt'

"""
dosya = open("kayit.txt", "r")
print(dosya.read(12))   # karakter okuma => Merhaba Berk
print(dosya.read()) # -AR
"""

with open("kayit.txt", "r") as dosya:
    print("İÇERİK 1")
    icerik = dosya.read()
    print(len(icerik), type(icerik))    # 15 <class 'str'>
    print(icerik)   # Merhaba Berk-AR   (bütün veriyi okudu)
    print("İÇERİK 2")
    icerik2 = dosya.read()
    print(len(icerik2), type(icerik2))  # 0 <class 'str'>
    print(icerik2)  # 