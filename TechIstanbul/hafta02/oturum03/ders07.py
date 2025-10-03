def toplama(a,b):
    sonuc = a + b
    return sonuc

def cikar(a,b):
    sonuc = a - b
    return sonuc

def carpma(a,b):
    sonuc = a * b
    return sonuc

def bolme(a,b):
    sonuc = a / b
    return sonuc

def yapIslem(a,b,islem):
    if islem == "toplama":
        return toplama(a,b)
    elif islem == "cikarma":
        return cikar(a,b)
    elif islem == "carpma":
        return carpma(a,b)
    elif islem == "bolme":
        return bolme(a,b)
    else:
        return "Geçersiz İşlem"
    
def karsilama():
    islem = input("Yapmak istediğiniz işlemi giriniz (toplama, cikarma, carpma, bolme): ")
    def alSayi():
        return float(input("Bir sayı giriniz: "))
    a = alSayi()
    b = alSayi()
    sonuc = yapIslem(a,b,islem)
    print(f"{a} {islem} {b} = {sonuc}")
    karsilama()

if __name__ == "__main__":
    print("Hesap makinesine hoşgeldiniz")
    karsilama()