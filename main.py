from flask import Flask, render_template, request, redirect, url_for, session
from clases import Auto

class MyApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.secret_key = 'clave_secreta'
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/', methods=['GET', 'POST'])
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

        @self.app.route('/agregar', methods=['GET', 'POST'])
        def agregar():
            if request.method == 'POST':
                tipo = request.form.get('tipo')
                marca = request.form.get('marca')
                modelo = request.form.get('modelo')
                precio = request.form.get('precio')
                cantidad = request.form.get('cantidad')
                descripcion = request.form.get('descripcion')
                urlImagen = request.form.get('urlImagen')

                # Verificar si algún campo está vacío
                if not tipo or not marca or not modelo or not precio or not cantidad or not descripcion or not urlImagen:
                    session['error'] = "Todos los campos son obligatorios"
                    return redirect(url_for('agregar'))

                nuevo_auto = Auto(tipo, marca, modelo, descripcion, precio, cantidad, urlImagen)
                Auto.agregarAuto(nuevo_auto)

                # Agregar un mensaje de éxito a la sesión
                session['success'] = f"Se ha registrado el auto con el idTipo: {tipo} correctamente"

            error = None
            if 'error' in session:
                error = session['error']
                session.pop('error', None)

            success = None
            if 'success' in session:
                success = session['success']
                session.pop('success', None)

            return render_template('agregar.html', error=error, success=success)

        @self.app.route('/info')
        def info():
            return render_template('info.html')

        @self.app.route('/registro')
        def registro():
            return render_template('registro.html')

    def run(self):
        self.app.run(host='localhost', debug=True)

if __name__ == '__main__':
    MyApp().run()