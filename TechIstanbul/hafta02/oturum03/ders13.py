def kontrolSifre(sifre):
    if len(sifre) < 8:
        return "Şifre en az 8 karakter olmalı"
    elif sifre.isnumeric():
        return "Şifre sadece sayı olamaz"
    elif sifre.isalpha():
        return "Şifre sadece harf olamaz"
    elif sifre.lower() == sifre:
        return "Şifre sadece küçük harf olamaz"
    elif sifre.upper() == sifre:
        return "Şifre sadece büyük harf olamaz"
    else:
        return "Şifre geçerli"
    pass

sifre = "Python123"
kontrolSifre(sifre)
print(kontrolSifre(sifre))