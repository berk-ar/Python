from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)   # Flask uygulaması nesnesi oluşturuldu

hazir_html = "hazır html kodları {}"

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/kullanici/<isim>')
def kullanici(isim):
    bugun = datetime.now().strftime("%d.%m.%Y")
    return render_template('kullanici.html', isim = isim, tarih = bugun)

if __name__ == "__main__":
    app.run(debug= True)