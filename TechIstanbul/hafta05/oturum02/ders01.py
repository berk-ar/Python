# Web Scraping = Web sayfalarından otomatik olarak veri çekme işlemidir.
# Kurulum için => pip install requests beautifulsoup4 lxml
"""
# Web scraping ile yapılabilecekler:
# - Haber sitelerinden son dakika haberlerini çekmek
# - E-ticaret sitelerinden ürün fiyatlarını takip etmek
# - Film/dizi sitelerinden en yüksek puanlı içerikleri bulmak
# - Sosyal medyadan trend konuları analiz etmek
"""

# ✅ YAPILABİLİR:
# - Public (herkese açık) verileri çekmek
# - robots.txt kurallarına uymak
# - Sunucuyu yormamak için bekleme süreleri koymak

# ❌ YAPILAMAZ:
# - Giriş gerektiren sayfaları hack'lemek
# - Telif hakkı olan içeriği kopyalamak
# - Sunucuyu aşırı yükleyecek şekilde sürekli istek atmak

"""
⚠️ Etik ve Yasal Uyarı:
Her site scraping’e izin vermez. robots.txt dosyası kontrol edilmeli, aşırı istek gönderilmemeli, 
telif hakkı ihlali yapılmamalıdır. 
"""

"""
pip install requests beautifulsoup4 lxml
requests: Web sayfasını indirmek için
beautifulsoup4: HTML’i işlemek için
lxml: HTML/XML parser (daha hızlı)
"""