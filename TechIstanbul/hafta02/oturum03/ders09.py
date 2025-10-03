def topla_cok(*sayilar):
    print(sayilar, type(sayilar))
    topla = 0
    for sayi in sayilar:
        topla += sayi
    print("toplam: ", topla)
    return topla

topla_cok(5,10,15)
topla_cok(5,10,15,20,25,30,35,40,45,50)

def ortalama(*args):
    toplam = 0
    for sayi in args:
        toplam += sayi
    ortalama = toplam / len(args)
    return ortalama

print(ortalama(3,5,7,9))    # 6.0
print(ortalama(3,5))        # 4.0