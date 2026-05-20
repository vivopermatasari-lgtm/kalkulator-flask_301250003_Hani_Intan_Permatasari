from flask import Flask, render_template, request, session
import math

app = Flask(__name__)
app.secret_key = 'kalkulator_secret_key_2025'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aritmatika', methods=['GET', 'POST'])
def aritmatika():
    hasil = None
    if request.method == 'POST':
        from calculator.aritmatika import hitung_aritmatika
        hasil = hitung_aritmatika(request.form)
        if 'history' not in session:
            session['history'] = []
        history = session['history']
        history.append(hasil.get('rumus', ''))
        session['history'] = history
    return render_template('aritmatika.html', hasil=hasil, history=session.get('history', []))

@app.route('/logika', methods=['GET', 'POST'])
def logika():
    hasil = None
    if request.method == 'POST':
        from calculator.logika import hitung_logika
        hasil = hitung_logika(request.form)
        if 'history_logika' not in session:
            session['history_logika'] = []
        history = session['history_logika']
        history.append(hasil.get('rumus', ''))
        session['history_logika'] = history
    return render_template('logika.html', hasil=hasil, history=session.get('history_logika', []))

@app.route('/transformasi', methods=['GET', 'POST'])
def transformasi():
    hasil = None
    if request.method == 'POST':
        from calculator.transformasi import hitung_transformasi
        hasil = hitung_transformasi(request.form)
        if 'history_transformasi' not in session:
            session['history_transformasi'] = []
        history = session['history_transformasi']
        history.append(hasil.get('ringkasan', ''))
        session['history_transformasi'] = history
    return render_template('transformasi.html', hasil=hasil, history=session.get('history_transformasi', []))

@app.route('/clear-history')
def clear_history():
    session.clear()
    return ('', 204)

if __name__ == '__main__':
    app.run(debug=True)