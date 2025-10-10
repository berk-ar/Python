# Kullanıcı uzunluk seçer, sistem karışık bir şifre üretir.

import random
import string

def sifreUret(uzunluk):
    karakterler = string.ascii_letters + string.digits + "!@#$%"
    return ''.join(random.choice(karakterler) for _ in range(uzunluk))
try:
    uzunluk = int(input("Şifre uzunluğu: "))
    print("Şifreniz: ", sifreUret(uzunluk))
except:
    print("Hata oluştu.")