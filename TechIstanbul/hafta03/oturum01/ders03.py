try:
    sayi1 = float(input("Birinci Sayıyı Giriniz: "))
    sayi2 = float(input("İkinci Sayıyı Giriniz: "))

    sonuc = sayi1 / sayi2

    print(f"Sonuç: {sayi1} / {sayi2} = {sonuc}")

except ZeroDivisionError:
    # Eğer sayi2 sıfır ise bu blok çalışır
    print("HATA: Bir sayıyı sıfıra bölemezsiniz!")

except ValueError:
    # Eğer kullanıcı sayı yerine metin girerse bu blok çalışır
    print("HATA: Lütfen geçerli bir sayı giriniz")

except:
    print("Beklenmeyen bir HATA")

print("Program sonlandı.")