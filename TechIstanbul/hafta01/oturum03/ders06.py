adet = int(input("Kaç dilim pizza istersiniz?: "))
dilim = adet
a = 1
while a <= adet:
    print(a, ". dilim pizzanız")
    a += 1

while dilim > 0:
    print("Afiyet olsun.")
    dilim -= 1