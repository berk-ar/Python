# default parametreli fonksiyon

def selamla(isim="Ziyaretçi"):
    print(f"Merhaba {isim} kursumuza hoşgeldiniz.")

selamla()
selamla("Berk")

def selamla(isim, mesaj= "Kursumuza hoşgeldin."):
    print(f"Merhaba {isim} {mesaj}")

selamla("Tuğba", "derse hoşgeldin.")

def hesaplaDaireAlan(r, pi=3.14):
    alan = r**2 * pi
    return alan

print(hesaplaDaireAlan(5))