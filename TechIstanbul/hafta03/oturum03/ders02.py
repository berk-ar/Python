import os

bulundugumDizin = os.path.dirname(os.path.abspath(__file__))
dosyaAdi = bulundugumDizin + "/" + "kayit.txt"

name = "Berk"
surname = "AR"

"""
Üç temel dosya formatı:
.txt -> Düz metin
.csv -> Virgülle ayrılmış değerler (Excel benzeri)
.json -> Yapılandırılmış veri (web, API'lerde çok kullanılır)
"""

# Bir dosya açalım ve içine bir şeyler yazalım
dosya = open(dosyaAdi, "w") # Dosyayı yazma modunda açıyoruz
dosya.write(f"Merhaba {name}-{surname} \nPython Bootcamp Kursu")   # Dosyanın içeriğine string yazdırıyoruz
dosya.close()   # Dosyayı kapatıyoruz
# Dosya kapatılmazsa kilitleniyor muhakkak kapatılması lazım

"""
# dosya.close() -> Kullanmamıza gerek kalmadan dosyayı otomatik olarak kapattı.
with open(dosyaAdi, "w") as dosya:
    dosya.write(f"Techistanbul Python Bootcamp'e Hosgeldin {name},{surname}")
"""

"""
# Dosya Açma Modları
w => yazma (varsa içeriği siler baştan yazar) eğer dosya yoksa dosyayı oluşturur
a => ekleme (dosyanın sonuna ekleme yapar) dosya yoksa oluşturur
r => dosyayı okur, dosya yoksa hata verir
x => dosyayı oluşturur, dosya varsa hata verir

t => modu text default mode ve metin işlemek için
b => binary mode (image dosyaları gibi)

rt => text modunda okuma
"""