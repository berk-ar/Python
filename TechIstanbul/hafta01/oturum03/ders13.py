hak = 3
dogru_sifre = "python123"

while hak > 0:
    sifre = input("Şifre giriniz: ")

    if sifre == dogru_sifre:
        print("Doğru şifre, giriş başarılı")
        break
    else:
        hak -= 1
        print("yanlış şifre girişi yaptınız.")
        print("kalan hakkınız", hak)
else:
    print("hesabınız bloke oldu.")