while True:
    try:
        yas = int(input("Yaşınızı giriniz: "))

        if yas < 0:
            raise ValueError("0'dan küçük yaş girişi yapılamaz.")

        dogumYili = 2025 - yas

        print(f"Doğum yılınız: {dogumYili}")
        break
    except ValueError:
        print("HATA: Lütfen sadece bir sayı girin! (Örnek: 25)")

        devam = input("Tekrar denemek için 'e', çıkmak için 'h' yazın: ")
        if devam.lower() == 'h':
            print("Program sonlandırıldı.")
            break
    finally:
        print("Teşekkür ederiz!")
