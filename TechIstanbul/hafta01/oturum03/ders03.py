baslangic = int(input("kaçtan başlayalım"))
bitis = int(input("kaça kadar"))
artis = int(input("artış değeri"))

for i in range(baslangic, bitis, artis):
    print(i)

print(list(range(5))) # [0, 1, 2, 3, 4]
print(list(range(1,5))) # [1, 2, 3, 4]
print(list(range(3,10,2))) # [3, 5, 7, 9]