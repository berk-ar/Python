meyveler = ["elma", "ananas", "çilek", "şeftali", "muz", "portakal"]

print(meyveler) # ['elma', 'ananas', 'çilek', 'şeftali', 'muz', 'portakal']
meyveler.append("limon") # .append() eleman ekleme
print(meyveler) # ['elma', 'ananas', 'çilek', 'şeftali', 'muz', 'portakal', 'limon']
print(meyveler.count("çilek")) # 1
print(meyveler.index("şeftali")) # 3
meyveler.insert(0, "kavun") # 0. index "kavun" eklendi.
print(meyveler)
meyveler[0] = "karpuz"
print(meyveler)

# Sıralama
meyveler.sort() # ['ananas', 'elma', 'karpuz', 'limon', 'muz', 'portakal', 'çilek', 'şeftali']
print(meyveler)
meyveler.reverse() # ['şeftali', 'çilek', 'portakal', 'muz', 'limon', 'karpuz', 'elma', 'ananas']
print(meyveler)

yeni_meyveler = ["üzüm", "kiraz"]
meyveler.extend(yeni_meyveler) # ['şeftali', 'çilek', 'portakal', 'muz', 'limon', 'karpuz', 'elma', 'ananas', 'üzüm', 'kiraz']
print(meyveler)

yeni_meyveler2 = ["kavun", "mango"]
meyveler.append(yeni_meyveler2) # ['şeftali', 'çilek', 'portakal', 'muz', 'limon', 'karpuz', 'elma', 'ananas', 'üzüm', 'kiraz', ['kavun', 'mango']]
print(meyveler)

meyveler.pop() # ['şeftali', 'çilek', 'portakal', 'muz', 'limon', 'karpuz', 'elma', 'ananas', 'üzüm', 'kiraz']
print(meyveler)

meyveler.remove("limon") # ['şeftali', 'çilek', 'portakal', 'muz', 'karpuz', 'elma', 'ananas', 'üzüm', 'kiraz']
print(meyveler)

del meyveler[5] # ['şeftali', 'çilek', 'portakal', 'muz', 'karpuz', 'ananas', 'üzüm', 'kiraz']
print(meyveler)

meyveler.clear() # []
print(meyveler)
"""
del meyveler # listeyi komple siler. name 'meyveler' is not defined.
print(meyveler)
"""