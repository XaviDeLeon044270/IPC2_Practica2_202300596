from flask import Flask, render_template, request, redirect, url_for, session
from clases import Auto

class MyApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.secret_key = 'clave'
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
                if username == 'empleado' and password == '$uper4utos#':
                    return redirect(url_for('agregar'))
                else:
                    session['error'] = "Usuario o contraseña incorrectos"
                    return redirect(url_for('index'))  
            return render_template('index.html', error=error)

        @self.app.route('/agregar', methods=['GET', 'POST'])
        def agregar():
            error = None
            success = None
            if request.method == 'POST':
                tipo = request.form.get('tipo')
                marca = request.form.get('marca')
                modelo = request.form.get('modelo')
                precio = request.form.get('precio')
                cantidad = request.form.get('cantidad')
                descripcion = request.form.get('descripcion')
                urlImagen = request.form.get('urlImagen')

                if any(auto.tipo == tipo for auto in Auto.obtenerAutos()):
                    error = 'Ya existe un auto con el mismo idTipoAuto.'
                    session['error'] = error
                else:
                    Auto.agregarAuto(tipo, marca, modelo, descripcion, precio, cantidad, urlImagen)
                    success = f"Se ha registrado el auto con el idTipo: {tipo} correctamente"
                    session['success'] = success

            if 'error' in session:
                error = session['error']
                session.pop('error', None)

            if 'success' in session:
                success = session['success']
                session.pop('success', None)

            return render_template('agregar.html', error=error, success=success)

        @self.app.route('/info')        
        def info():
            return render_template('info.html')

        @self.app.route('/registro', methods=['GET', 'POST'])
        def registro():
            if request.method == 'POST':
                idTipo_eliminar = request.form.get('eliminar')
                if idTipo_eliminar:
                    Auto.eliminarAuto(idTipo_eliminar)
            autos = Auto.obtenerAutos()
            return render_template('registro.html', autos=autos)

    def run(self):
        self.app.run(host='localhost', port=5000, debug=True)

if __name__ == '__main__':
    MyApp().run()

        