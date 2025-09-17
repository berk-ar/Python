yol = float(input("Ne kadar yol gittiniz: "))
zaman = float(input("Ne kadar zamanda gittiniz: "))
hiz = yol / zaman

if hiz >= 132:
    print(f"Hız sınırını aştınız: {hiz}")
    print(f"hız sınırını {hiz - 132} kadar aştınız")
else:
    print(f"Hız sınırını aşmadınız hızınız: {hiz}")
    print("Hız kurallarına uyduğunuz için teşekkürler")