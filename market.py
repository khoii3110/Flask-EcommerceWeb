from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>hello worldđ</h1>'

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = [
        {'id':1,'name':'Phone','barcode':'222332','price':334}
        ,{'id':2,'name':'Laptop','barcode':'223233223','price':223},
        {'id':3,'name':'Keyboard','barcode':'22332832','price':223}
    ]
    return render_template('market.html',items=items)