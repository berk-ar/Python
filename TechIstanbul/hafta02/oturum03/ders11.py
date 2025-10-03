# kısa tek satırlı fonksiyonlar için kullanılır

kare_al = lambda x: x**2

print(kare_al(5))   # 25
print(kare_al(9))   # 81

ogrenciler = [("berk", 25), ("tuğba", 25), ("rafa", 27)]

siralama = sorted(ogrenciler, key = lambda x: x [1], reverse= True)
print(siralama)

siralama2 = sorted(ogrenciler, key = lambda x: x [0], reverse= True)
print(siralama2)

# lambda ile filtreleme

sayilar = [1,2,3,4,5,6,7,8,9,10]
cift_sayilar = list(filter(lambda x: x % 2 == 0, sayilar))
print("Çift Sayılar:", cift_sayilar)    # Çift Sayılar: [2, 4, 6, 8, 10]

# lambda ile liste dönüştürme
kareler = list(map(lambda x: x**2, sayilar))
print("Kareler:",kareler)   # Kareler: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]