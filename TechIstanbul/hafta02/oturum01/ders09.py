ogrenciler = {"berk", "tuğba", "quaresma", "atiba", "fabri"}
print(ogrenciler)
print(type(ogrenciler)) # <class 'set'>

# boskume = set()
# print(boskume)  # set()

for ogrenci in ogrenciler:
    print(ogrenci)

ogrenciler.add("rafa")
print(ogrenciler)

ogrenciler.remove("fabri")
print(ogrenciler)