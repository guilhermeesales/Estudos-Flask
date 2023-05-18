# Aula 16 - REST API Parte 2 

from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from controllers.estudante import app as estudante_controller

db = SQLAlchemy()
app = Flask(__name__, template_folder="templates")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estudantesjson.sqlite3'


app.register_blueprint(estudante_controller, url_prefix="/estudante/")

if __name__ == '__main__':
        
    db.init_app(app=app)

    with app.app_context():
        db.create_all()

    app.run(debug=True)