dogum_yili = int(input("Doğum yılınızı giriniz: "))
yas = 2025 - dogum_yili

if yas >= 18:
    print("Ehliyet alabilirsiniz.")
else:
    print("Ehliyet alacak yaşta değilsiniz.")
    print(18 - yas, "yıl sonra ehliyet alabilirsiniz.")
    print(f" ehliyet almak için {18-yas} yıl beklemeniz gerekir.")
    print(f"ehliyet alamazsınız çünkü {yas} yaşındasınız.")