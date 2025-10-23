from bs4 import BeautifulSoup

html_content = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Öğrenci Listesi</title>
</head>
<body>
    <div id="main" class="content">
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

soup = BeautifulSoup(html_content, "html.parser")

print(soup.select_one(".content").text)
print("-----------------------------------")
print(soup.select(".student")[1].text)  # Tuğba AR