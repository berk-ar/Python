birlesik = ""

while True:
    metin = input("Bir metin giriniz: ")
    if metin.lower() == "exit":
        print(birlesik)
        print("Çıkış yapıldı.")
        break
    else:
        birlesik += metin