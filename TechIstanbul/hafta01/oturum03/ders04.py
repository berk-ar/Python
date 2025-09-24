toplam = 0
carpim = 1
for dd in range(1,11):
    print(dd)
    toplam = toplam + dd
    print("Toplam: ",toplam, dd)
    carpim = carpim * dd
    print("Çarpım: ", carpim, dd)

print("--------------------------------------")

adet = int(input("kaç dilim pizza istersiniz?: "))
for dilim in range(adet):
    print(dilim+1, ". dilim pizzanız")