yemek = input("Yemek siparişinizi giriniz: ")
icecek = input("İçecek siparişinizi giriniz: ")

if yemek == "pizza" and icecek == "kola":
    print("Geçerli sipariş")
    print("Afiyet olsun.")
else:
    print(f"{yemek} - {icecek} ikilisi doğru bir sipariş değil.")