from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Aprendiendo Flask con Milton Ponce"

@app.route('/informacion/<string:nombre>/<int:apellidos>')
def informacion(nombre, apellidos):
    return f"""
        <h1>Página de Información</h1>
        <p>Esta es la página de información</p>
        <h3>Bienvenido, {nombre} {apellidos}</h3>
    """

@app.route('/contacto')
def contacto():
    return "<h1>Página de Contacto</h1>"

@app.route('/lenguajes-de-programacion')
def lenguajes():
    return "<h1>Página de Lenguajes</h1>"

if __name__ == '__main__':
    app.run(debug=True)
