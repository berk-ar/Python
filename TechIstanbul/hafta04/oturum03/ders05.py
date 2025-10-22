import sqlite3
import os

bulundugumDizin = os.path.dirname(os.path.abspath(__file__))
veritabani = bulundugumDizin + "/" + "kutuphane.db"
baglanti = sqlite3.connect(veritabani)
imlec = baglanti.cursor()

imlec.execute("SELECT * FROM kitaplar")

kitaplar = imlec.fetchall()
print(kitaplar) # [(1, 'Kotlin', 'Berk'), (2, 'Python', 'Tuğba')]

for i in kitaplar:
    print(i)

baglanti.close()