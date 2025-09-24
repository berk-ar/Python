# Kullanıcıdan bir cümle al, kaç tane 'a' harfi olduğunu say.

cumle = input("Bir cümle giriniz: ")
sayac = 0

for harf in cumle:
    if harf.lower() == "a" or harf == "A":
        sayac += 1
print(f"'{cumle}' içerisinde {sayac} tane a-A var.")