from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Estudante(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column('nome', db.String(150))
    idade = db.Column('idade', db.Integer)

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    
    def to_dict(self, colums=[]):
        if not colums:   # se tiver vazio
            return { 'id': self.id, 'nome': self.nome, 'idade': self.idade }
        else:
            return { col: getattr(self, col) for col in colums }
                