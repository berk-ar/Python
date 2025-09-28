treng = {"araba": "car", "kalem": "pencil", "kırmızı": "red"}

print(treng)    # {'araba': 'car', 'kalem': 'pencil', 'kırmızı': 'red'}

for key, value in zip(treng.keys(), treng.values()):
    print(key, "=>", value)