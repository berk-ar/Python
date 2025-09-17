ad = "BerkAR"
boyut = len(ad)
print(boyut)
print(ad[0])
print(ad[5])
#print(ad[başlangıç:bitiş])
print(ad[0:4])
#print(ad[başlangıç:bitiş:artış])
print(ad[0:4:2])

print("Be" in ad) # true
print("Berk" in ad) # true
print("Ar" in ad) # false

print(ad.upper()) # BERKAR
print(ad.lower()) # berkar