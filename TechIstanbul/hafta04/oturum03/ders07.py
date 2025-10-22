import sqlite3
import os

bulundugumDizin = os.path.dirname(os.path.abspath(__file__))
veritabani = bulundugumDizin + "/" + "kutuphane.db"
baglanti = sqlite3.connect(veritabani)
imlec = baglanti.cursor()

imlec.execute("DELETE FROM kitaplar WHERE id=?", (3,))

baglanti.commit()
baglanti.close()