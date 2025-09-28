sayilar = [1,2,3,4,5,6]
kareler = {x: x**2 for x in sayilar}
print(kareler)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}

kelimeler = ["berk", "tuğba"]
harf_sayili = { kelime: len(kelime) for kelime in kelimeler }
print(harf_sayili)  # {'berk': 4, 'tuğba': 5}