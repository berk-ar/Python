import sqlite3
import os

bulundugumDizin = os.path.dirname(os.path.abspath(__file__))
veritabani = bulundugumDizin + "/" + "kutuphane.db"
baglanti = sqlite3.connect(veritabani)
imlec = baglanti.cursor()
try:
    # Tablo oluşturma sorgusu
    imlec.execute(
        """CREATE TABLE kitaplar(
            id INTEGER PRIMARY KEY,
            ad TEXT,
            yazar TEXT
        )"""
    )

    baglanti.commit()   # Değişiklikleri kaydet eğer imleç aracılığı ile gerçekleştirdiğimiz işlemler var ise
except Exception as e:
    print(e)    # table kitaplar already exists
baglanti.close()
print("Kitaplar tablosu oluşturuldu (veya zaten vardı).")