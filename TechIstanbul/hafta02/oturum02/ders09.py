yemekler = {
    "Çorbalar": {"Etli": ["işkembe", "kelle paça"],
                 "Bakliyatlı": ["mercimek", "ezogelin"],
                 "Sebzeli":["mantar", "brokoli"]},
    "Kebaplar": {"Acılı": ["adana", "mardin"], 
                "Acısız": ["urfa", "antep"], 
                "Dürüm": ["adana dürüm", "urfa dürüm"]},
    "İçecekler": ["Çay", "Kahve"]
}

print(yemekler)

for anakategori in yemekler:
    print(anakategori)
    if type(yemekler[anakategori]) is dict:
        for altkategori in yemekler[anakategori]:
            print("\t", altkategori)
            if type(yemekler[anakategori][altkategori]) is dict:
                for altkategori2 in yemekler[anakategori][altkategori]:
                    print("\t\t", altkategori2)
                    for altkategori3 in yemekler[anakategori][altkategori][altkategori2]:
                        print("\t\t\t", altkategori3)
            else:
                print("\t\t", yemekler[anakategori][altkategori])
    else:
        print("\t", yemekler[anakategori])