ogrenci_adi = "Berk"
ogrenci_yas = 25
ogrenci_katilim = True

ogrenci1 = [ogrenci_adi, ogrenci_yas, ogrenci_katilim]
print(ogrenci1) # ['Berk', 25, True]
print(type(ogrenci1)) # <class 'list'>

ogrenci2 = ["Tuğba", 25, True] # ['Tuğba', 25, True]
print(ogrenci2)
print(type(ogrenci2)) # <class 'list'>

print(ogrenci2[0]) # Tuğba 
print(type(ogrenci2[0])) # <class 'str'>

print(len(ogrenci2)) # 3    -> elemanlı bir liste

print("b" in ogrenci2) # False

for bilgi in ogrenci2:
    print(bilgi) #  Tuğba 25 True

print("--------------------------------------")

for i in range(len(ogrenci2)):
    print(ogrenci2[i])  #  Tuğba 25 True

