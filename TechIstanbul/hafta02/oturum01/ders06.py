sebze = ["patates", "soğan"]
meyve = ["elma", "armut"]
sark = ["peynir", "bal"]
yesillik = ["maydonoz", "roka", "semiz otu"]

# pazar_listesi = sebze + meyve + sark + yesillik

# print(pazar_listesi) # ['patates', 'soğan', 'elma', 'armut', 'peynir', 'bal', 'maydonoz', 'roka', 'semiz otu']
# print(len(pazar_listesi)) # 9

pazar_listesi2 = [sebze, meyve, sark, yesillik,]
pazar_listesi2.append("sütlaç")
print(pazar_listesi2) # [['patates', 'soğan'], ['elma', 'armut'], ['peynir', 'bal'], ['maydonoz', 'roka', 'semiz otu']]
print(pazar_listesi2[0]) # ['patates', 'soğan']  
print(pazar_listesi2[0][0]) # patates
print(pazar_listesi2[3][2]) # semiz otu

for kategori in pazar_listesi2:
    print(kategori)
    if type(kategori) != list:
        continue
    for urun in kategori:
        print("\t", urun)