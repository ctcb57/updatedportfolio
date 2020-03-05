from flask import Flask, render_template, url_for
app = Flask(__name__)



@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/about')
def blog():
    return render_template('about.html')

