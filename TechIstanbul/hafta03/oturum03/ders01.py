# Scope, bir değişkenin, fonksiyonun veya nesnenin nerede tanımlandığı ve nerelerden erişilebildiği bilgisidir
# Python'da her isim(değişken, fonksiyon, sınıf vb.) bir kapsam (scope) içinde yaşar.
# Bu kapsam, o ismin geçerli olduğu bölgeyi belirler.

# Python, isim araması yaparken LEGB kuralını takip eder:

# L Local Mevcut fonksiyon/metot içinde tanımlananlar
# E Enclosing İç içe fonksiyon varsa, dıştaki fonksiyonun scope'u
# G Global Modül (dosya) seviyesinde tanımlananlar
# B Built-in Python'un yerleşik isimleri (len, print, int vs.)
# Python bir ismi ararken: Local -> Enclosing -> Global -> Built-in sırasıyla bakar.

# Local scope
def fonksiyon1():
    x = 50
    print(x)
fonksiyon1() # 50

print("-------------------------------------")

# Fonksiyonlar içinde scope Enclosing
def ustFonksiyon1():
    x = 300
    def altFonksiyon1():
        print(x)
        # x = 400 # => UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
    altFonksiyon1()
ustFonksiyon1()  # 300

print("-------------------------------------")

# Global scope

x = 17
def fonksiyon2():
    print(x)
    # x = 18  # => UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
print(x)    # 17
fonksiyon2() # 17

print("-------------------------------------")

# Global keyword ile global değişkenlere erişim ve değişiklikler yapma

sayi = 1000
def sayiFonksiyon():
    global sayi
    sayi = 1903
    print(sayi)
print(sayi) # 1000
sayiFonksiyon() # 1903
print(sayi) # 1903

def sayiFonksiyon2():
    global sayi2    # dışarıdan da erişim sağlanır.
    sayi2 = 1453
    print(sayi2)
sayiFonksiyon2()    # 1453
print(sayi2)    # 1453

print("-------------------------------------")

# Nonlocal keyword

def ustFonksiyon2():
    isim = "berk"
    def altFonksiyon2():
        nonlocal isim
        isim = "berk ar"
    print(isim)
    altFonksiyon2()
    print(isim)

ustFonksiyon2()