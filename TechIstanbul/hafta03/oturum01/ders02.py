while True:
    try:
        isim = input("İsminizi Giriniz: ")
        if len(isim) < 2:
            raise ValueError("İsim bilgisi en az 2 karakter olmalı")
        yas = int(input("Yaşınızı Giriniz: "))
        if yas < 0 or yas > 150:
            raise ValueError("Yaş aralığı 0-150 arasında olmalı")
    except ValueError as e:
        print("Hata: ",e)
    except Exception as e:
        print("Exception Hata: ", e)
    else:
        print("Hoş Geldiniz.") # Try ifadesi bir exception ile karşılaşmazsa çalışır.
        break # While döngüsünden çıkmak için
    finally:
        print("Bu son blok her zaman işletilir.") # Try ifadesi exception yakalasa bile çalışır.