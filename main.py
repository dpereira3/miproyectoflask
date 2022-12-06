from flask import Flask, redirect, url_for, render_template, request, flash

app = Flask(__name__)

@app.before_request
def before_request():
    #print("Antes de la peticion")
    pass

@app.after_request
def after_request(response):
    #print("Despues de la peticion")
    return response

@app.route('/')
def index():
    flash('Has iniciado en la pagina principal')
    print("accediendo al index")
    datos = {'titulo':'Pagina principal','encabezado':'Bienvenido a mi pagina web'}
    #Datos a mostrar como diccionario
    #encabezado = "Encabezado desde Flask"
    return render_template('index.html',datos = datos)
    #return "Este es el INDEX o pagina principal"

@app.route('/acercade')
def acercade():
    dic = {'titulo':'Acerca de','encabezado':'Acerca de mí'}
    #return "<h1>Acerca de mi</h1>"
    return render_template('acercade.html', datos = dic)

@app.route('/condicionybucle')
def condicionybucle():
    datos = {
        'edad': 50,
        'nombres' : ['Jose','Mar','Lucia','Eva']
    }
    return render_template('condicionybucle.html', datos = datos)

#Con parametros
@app.route('/saludame/<string:nombre>')
@app.route('/saludame/<string:nombre>/<int:edad>')
def saludame(nombre,edad=None):
    if edad != None:
        return "Hola {} tienes {} años.".format(nombre, edad)
    else:
        return f"""
            <h1>Hola, </h1>
            <h3>{nombre}</h3>
            """
#Con parametros y funcion sumar
@app.route('/suma/<int:numero1>/<int:numero2>')
def suma(numero1,numero2):
    suma = numero1 + numero2
    return f"""La suma es ingual a {suma}"""

#Redireccion
@app.route('/redirecciona')
@app.route('/redirecciona/<string:sitio>')
def redirecciona(sitio=None):
    if sitio is not None:
        return redirect(url_for('index'))
    else:
        return redirect(url_for('acercade'))

#Pagina no encontrada
def pagina_no_encontrada(error):
    return render_template('errores/404.html'), 404

if __name__ == '__main__':
    app.register_error_handler(404, pagina_no_encontrada)
    app.secret_key = 'clave-flask'
    app.run(debug=True)

