from flask import Flask, render_template, url_for, request
app = Flask(__name__,template_folder='template')

@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/scan')
def scan_page():
    return render_template('scan.html')


@app.route('/pricing', methods=['POST'])
def pricing_page():
    adress = request.form.get("s")
    items = [
    {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
    {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
    {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    return render_template('pricing.html', items=items, adress=adress)
