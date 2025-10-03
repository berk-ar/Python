def selamla(isim):
    print(f"Merhaba {isim} kursumuza hoşgeldiniz")
    if len(isim) < 5:
        return True
    else:
        return False
    
ad = input("İsminizi giriniz: ")
sonuc = selamla(ad)
print(sonuc, type(sonuc))   # True <class 'bool'>

if sonuc:
    print("isminiz 5 karakterden kısa")
else:
    print("isminiz 5 karakterden uzun")