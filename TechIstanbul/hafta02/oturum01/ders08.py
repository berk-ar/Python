demet = (25, False, "Berk", ["Berk", "İngilizce"],(25, True, "Tuğba", ["Tuğba", "İngilizce"]))
print(demet)
print(type(demet)) # <class 'tuple'>

pazar = ["elma", "armut"]
pazarDemeti = tuple(pazar)
print(pazarDemeti)  # ('elma', 'armut')
print(type(pazarDemeti))    # <class 'tuple'>

print(demet.index("Berk"))  # 2
print(demet.count("İngilizce")) # 0

for eleman in demet:
    print(eleman)

dlist = list(demet)
dlist[1] = True

demet = tuple(dlist)
print(demet)

print(demet[:3])    # (25, True, 'Berk')
print(demet[::-1])