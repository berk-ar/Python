def fibonacci(adet):
    seri = []
    a, b = 0, 1
    for _ in range(adet):
        seri.append(a)
        a, b = b, a+b
    return seri

print(fibonacci(12))    # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def faktoriyel(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktoriyel(n-1)
    
print(faktoriyel(4))    # 24

def yazTersten(metin):
    if len(metin) == 0:
        return metin
    else:
        # return metin[-1] + yazTersten(metin[:-1])
        return yazTersten(metin[1:]) + metin[0]
    
print(yazTersten("Berk"))   # kreB
print(yazTersten("Tuğba"))  # abğuT