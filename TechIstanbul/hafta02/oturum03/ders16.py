def ogrenci_ortalama_hesapla(ogrenci):
    notlar = ogrenci.get("notlar", [])
    if not notlar:
        return 0
    toplam = sum(notlar)
    ortalama = toplam / len(notlar)
    return ortalama

def student_score_average(student):
    total = 0
    for score in student['scores']:
        total += score
    average_score = total / len(student['scores'])
    return average_score

ogrenci = {"ad": "Berk", "notlar": [90,95,99,100]}
ortalama = ogrenci_ortalama_hesapla(ogrenci)
print(f"{ogrenci['ad']} isimli öğrencinin not ortalaması: {ortalama}")

student = {"name": "Berk", "scores": [95,99,100,98]}
average = student_score_average(student)
print(f"{student['name']} isimli öğrencinin not ortalaması: {average}")