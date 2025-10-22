import sqlite3
import os

bulundugumDizin = os.path.dirname(os.path.abspath(__file__))
veritabani = bulundugumDizin + "/" + "kutuphane.db"
baglanti = sqlite3.connect(veritabani)
imlec = baglanti.cursor()

imlec.execute("UPDATE kitaplar SET ad=? WHERE id=?", ("Kotlin ile Uygulama Geliştirme", 1))

baglanti.commit()
baglanti.close()