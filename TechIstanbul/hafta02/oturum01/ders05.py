adet = int(input("Kaç tane alet alacaksınız?: "))
aletler = []
for i in range(1, adet+1):
    print(i, ". ne alacaksınız")
    urun = input("ürün : ")
    aletler.append(urun)

print(aletler)

for urunler in aletler:
    print(urunler)