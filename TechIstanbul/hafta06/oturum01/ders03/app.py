from flask import Flask, render_template, url_for, redirect, request
app = Flask(__name__)

app.secret_key = 'Af34dfgDFHdfh43623'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/user/<username>')
def user(username):
    return render_template('user.html', username = username)

@app.route('/anasayfa')
def anasayfa():
    # return redirect(url_for('index'))
    return redirect('https://google.com')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug= True)