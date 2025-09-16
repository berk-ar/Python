# değişkenler ve veri tipleri
# değişken tanımlama kuralları
# 1.harf veya _ ile başlamalı
# 2. sayı ile başlayamaz
# 3. türkçe karakter kullanılmaz (kullanılmamalı farklı sistemlerde sorun oluşturabilir)
# 4. boşluk kullanılmaz
# 5. özel karakter kullanılmaz -> _ harici
# 6. büyük küçük harf duyarlılığı
# 7. anahtar kelimeler kullanılmaz (for not if elif while .... gibi)

# değişken tanımlama

# değişken = değer
# değer atama işlemi sağdan sola doğrudur
# atama işlemi için = kullanılır
# değişken isimleri anlamlı olmalıdır.
# bir değişkene atanan değer istediğimiz zaman değiştirilebilir.

ad = "techistanbul"
print(ad)
print(type(ad)) # str
sayi = 5
print(sayi)
print(type(sayi)) # int
print(sayi == 8) # false
print(sayi * 2) # 10