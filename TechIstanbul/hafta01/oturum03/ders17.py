# Kullanıcıdan bir metin al, onu tersten yazdır.
"""
kelime = input("Bir kelime giriniz: ")
ters = ""

for i in range(len(kelime)-1, -1, -1):
    ters += kelime[i]
print("Tersten yazılışı: ", ters)
"""

"""
cumle = input("Bir cümle giriniz: ")
sayac = 0
tersi = ""

for harf in cumle:
    sayac -= 1
    print(cumle[sayac])
    tersi += cumle[sayac]
print(tersi)
"""

metin = input("Bir metin giriniz: ")
ters = ""
for harf in metin:
    ters = harf + ters
    print(ters)
print("Ters hali: ", ters)