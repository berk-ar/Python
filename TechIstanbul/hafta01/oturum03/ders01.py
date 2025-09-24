#print(range(10))   => range(0, 10)
#print(list(range(10)))     => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for dd in range(10): # 0,1,2,3,4,5,6,7,8,9 (10 hariç)
    print(f"{dd+1}.dilim pizzanız") # 1'den başlar 10'a kadar gider.

print("----------------------")

for harf in "Berk": # B e r k
    print(harf)

print("----------------------")

isim = "Berk"
for name in isim[:3]: # B e r
    print(name)