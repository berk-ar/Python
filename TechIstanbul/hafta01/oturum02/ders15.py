ad1 = "Berk"
ad2 = "Kartal"

metin = "Merhaba Sayın {} Python Bootcamp'e Hoşgeldiniz."

print(metin.format(ad1))
print(metin.format(ad2))

metin2 = "Yarışmamızın 1.si {} , 2.si {}"

print(metin2.format(ad1, ad2))
print(metin2.count("m"))