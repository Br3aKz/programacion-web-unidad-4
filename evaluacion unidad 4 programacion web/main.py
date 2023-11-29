from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = 'clave'

usuarios = {'juan': 'admin', 'pepe': 'user'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None

    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])

        precio_tarro = 9000
        total_sin_descuento = tarros * precio_tarro

        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        descuento_aplicado = total_sin_descuento * descuento
        total_con_descuento = total_sin_descuento - descuento_aplicado

        resultado = {
            'nombre': nombre,
            'total_sin_descuento': total_sin_descuento,
            'descuento_aplicado': descuento_aplicado,
            'total_con_descuento': total_con_descuento
        }

    return render_template('ejercicio1.html', resultado=resultado)

@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')

@app.route('/procesar_ejercicio2', methods=['POST'])
def procesar_ejercicio2():
    usuario = request.form['usuario']
    contrasena = request.form['contrasena']

    if usuario in usuarios and usuarios[usuario] == contrasena:
        if usuario == 'juan':
            mensaje = 'Bienvenido administrador juan'
        elif usuario == 'pepe':
            mensaje = 'Bienvenido usuario pepe'
        else:
            mensaje = 'Bienvenido ' + usuario
    else:
        mensaje = 'Usuario o contraseña incorrectos'

    return render_template('ejercicio2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)