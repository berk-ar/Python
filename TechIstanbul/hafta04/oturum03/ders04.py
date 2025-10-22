"""
CRUD (Create, Read, Update, Delete) bir veri tabanı uygulamasının temel dört işlemidir.
"""

import sqlite3
import os

bulundugumDizin = os.path.dirname(os.path.abspath(__file__))
veritabani = bulundugumDizin + "/" + "kutuphane.db"
baglanti = sqlite3.connect(veritabani)
imlec = baglanti.cursor()

kitapAdi = input("Kitap adı giriniz: ")
kitapYazari = input("Yazar giriniz: ")

imlec.execute("INSERT INTO kitaplar VALUES(NULL, ?, ?)", (kitapAdi, kitapYazari))

baglanti.commit()
print(kitapAdi, "kitabı veri tabanına kaydedildi.")
baglanti.close()