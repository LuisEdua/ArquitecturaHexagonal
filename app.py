from flask import Flask
from MateriasTemas.Infrestructure.Route.MateriaRoute import materia_blueprint
from MateriasTemas.Infrestructure.Route.TemaRoute import tema_blueprints

app = Flask(__name__)

app.register_blueprint(materia_blueprint, url_prefix="/materia")
app.register_blueprint(tema_blueprints, url_prefix="/tema")

if __name__ == "__main__":
    app.run(debug=True, port=3000)
