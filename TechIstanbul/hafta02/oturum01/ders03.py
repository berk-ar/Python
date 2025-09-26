ad = "Berk"
adHarfleri = list(ad)
print(adHarfleri) # ['B', 'e', 'r', 'k']
print(len(adHarfleri)) # 4  -> elemanlı bir dizi


# Tekrar string'e dönüştürme ancak yanlış bir dönüştürme olur.
yeniString = str(adHarfleri)
print(yeniString) # ['B', 'e', 'r', 'k']
print(len(yeniString)) # 20 -> elemanlı bir string????
print(type(yeniString)) # <class 'str'>