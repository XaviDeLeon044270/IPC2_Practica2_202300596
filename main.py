from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'clave_secreta'

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if 'error' in session:
        error = session['error']
        session.pop('error', None)

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'a' and password == 'a':
            return redirect(url_for('agregar'))
        else:
            session['error'] = "Usuario o contraseña incorrectos"
            return redirect(url_for('index'))  
    return render_template('index.html', error=error)

@app.route('/agregar')
def agregar():
    return render_template('agregar.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

if __name__ == '__main__':
    app.run(host='localhost', debug=True)