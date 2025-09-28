oyuncular = {
    "bjk" : ["rafa", "orkun", "abraham"],
    "fb" : ["asensio", "ederson", "fred"],
    "gs" : ["osimhen", "sane", "icardi"]
}

print(oyuncular["bjk"]) # ['rafa', 'orkun', 'abraham']
print(oyuncular["fb"])  # ['asensio', 'ederson', 'fred']
print(oyuncular["gs"])  # ['osimhen', 'sane', 'icardi']

for takim in oyuncular:
    print(takim)
    # print(oyuncular[takim])
    for oyuncu in oyuncular[takim]:
        print("\t", oyuncu)