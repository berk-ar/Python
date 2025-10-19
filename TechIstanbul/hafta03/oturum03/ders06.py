import os

# Dosya silme işlemi
bulundugumDizin = os.path.dirname(os.path.abspath(__file__))
dosyaAdi = bulundugumDizin + "/" + "kurs.txt"

if os.path.exists(dosyaAdi):
    os.remove(dosyaAdi)
    print("Dosya başarılı şekilde silindi.")
else:
    print("Silinecek dosya bulunamadı.")