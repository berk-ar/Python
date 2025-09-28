# ornek1
"""
kareler = []
for i in range(1,11):
    kareler.append(i**2)
print(kareler)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

sayilar = list(range(1,11))
print(sayilar)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
kareler = [x**2 for x in sayilar]
print(kareler)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""

# ornek2
"""
cift_sayilar = []
for i in range(1,21):
    if i % 2 == 0:
        cift_sayilar.append(i)
print(cift_sayilar) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

ciftler = [x for x in range(1,21) if x % 2 == 0]
print(ciftler)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
"""

cumle = "TechIstanbul Python Bootcamp"
kelimeler = cumle.split()
print(kelimeler)    # ['TechIstanbul', 'Python', 'Bootcamp']
uzunluklar = [len(kelime) for kelime in kelimeler]

for kelime, uzunluk in zip(kelimeler, uzunluklar):
    print(kelime, uzunluk)