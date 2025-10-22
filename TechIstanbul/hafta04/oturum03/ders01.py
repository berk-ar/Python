"""
Tıpkı bir kütüphanenin kitapları düzenlemesi gibi, veritabanları da bilgileri düzenler.

Neden?: Programımız kapandığında kaybolmasını istemediğimiz bilgileri (kullanıcı bilgileri, ürün listesi, notlar vb.)
kalıcı olarak saklamak için gereklidir.

SQLite Nedir?: Veritabanının tamamını tek bir dosyada saklayan, hafif ve kurulum gerektirmeyen bir veritabanı motorudur.
Python ile kullanılması çok kolaydır.
"""

# Python'da veritabanı işlemlerini yapmak için standart olarak gelen sqlite3 modülünü kullanılır.

# Veritabanıyla konuşmak için önce bir bağlantı (connection) kurmalıyız.

import sqlite3
# import os

# bulundugumDizin = os.path.dirname(os.path.abspath(__file__))
# veritabani = bulundugumDizin + "/" + "kutuphane.db"
# baglanti = sqlite3.connect(veritabani)

baglanti = sqlite3.connect("C:/PythonEdu/Python/TechIstanbul/hafta04/oturum03/kutuphane.db")

baglanti.close()