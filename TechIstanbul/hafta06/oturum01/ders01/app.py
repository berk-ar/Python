from flask import Flask

app = Flask(__name__)   # Flask uygulaması nesnesi oluşturuldu

@app.route("/anasayfa") # Anasayfa URL
@app.route("/index") # Anasayfa URL
@app.route("/") # Anasayfa URL
def index():
    return "Merhaba TechIstanbul Python Bootcamp'e Hoşgeldiniz."

@app.route("/hakkimizda")
def hakkimizda():
    return "Hakkımızda sayfasındasınız"

@app.route("/kullanici/<isim>/<soyisim>")
def kullanici(isim, soyisim):
    return f"Kullanıcı sayfasındasınız: {isim} - {soyisim}"

@app.route('/yil/<int:year>')
def yilGoster(year):
    return f"Şuan {year} yılındayız."

if __name__ == "__main__":
    app.run(debug= True)