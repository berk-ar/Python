import sqlite3

# 'kutuphane.db' adında bir veritabanı dosyasına bağlan.
# Eğer dosya yoksa, otomatik olarak oluşturulur.

baglanti = sqlite3.connect("C:/PythonEdu/Python/TechIstanbul/hafta04/oturum03/kutuphane.db")

# Veri tabanı ile bağlantı kurulduğunda, işlem yapabilmemiz için nesnenin oluşturulması gerekir.
# İşaretçi nesnesi bağlantı nesnesinin cursor() özelliği ile oluşturulur.
imlec = baglanti.cursor() # İşlemci oluşturuldu
# ... sorgular burada çalışır ...
# Bağlantıyı bitir, bu önemli!

baglanti.close()