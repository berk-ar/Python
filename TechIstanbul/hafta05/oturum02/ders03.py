from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Öğrenci Listesi</title>
</head>
<body>
    <div id="main">
        <h1 id="class-title">10-A Sınıfı</h1>
        <ul>
            <li class="student">Berk AR</li>
            <li class="student">Tuğba AR</li>
            <li class="student">Student 3</li>
        </ul>
    </div>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, "html.parser")

print("1. tag ismine göre işlem", soup.title.text)
print("1. tag ismine göre işlem", soup.div.text)
print("1. tag ismine göre işlem", soup.h1.text)
print("2. id ile işlem yapmak", soup.find(id="class-title").text)
print("3. class ile işlem yapmak", soup.find(class_="student").text)

tum_ogrenciler = soup.find_all(class_="student")
print(tum_ogrenciler, type(tum_ogrenciler))
for o in tum_ogrenciler:
    print("Öğrenci:", o.text)