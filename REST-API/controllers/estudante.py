from flask import Blueprint, Response, request
from ..models.models import db, Estudante
import json

app = Blueprint("Estudantes", __name__)   # Referencia a nossa main

@app.route('/')
def index():
    estudantes = Estudante.query.all()
    result = [estudante.to_dict() for estudante in estudantes]
    return Response(response=json.dumps(result), status=200, content_type="application_json")


@app.route('/view/<int:id>', methods=['GET'])
def view(id):
    row = Estudante.query.filter_by(id=id).first()
    if row is None:   # Não foi encontrado nada
        return Response(response=json.dumps({'filtro': 'Indisponível'}), status=200, content_type="application_json")
    return Response(response=json.dumps(row.to_dict()), status=200, content_type="application_json")


@app.route('/add', methods=["POST"])
def add():
    estudante = Estudante(request.form['nome'], request.form['idade'])  # Vamos passar o nome e a idade do aluno
    print(request.form['nome'], request.form['idade'])
    db.session.add(estudante)  # Adicionar os dados enviados
    db.session.commit()   # Enviar os dados pro banco
    return app.response_class(response=json.dumps({'status': 'sucess', 'data': estudante.to_dict()}), status=200, content_type="application_json")
    

@app.route('/edit')
def home():
    return app.response_class(response=json.dumps({'resultado': 'Rota não encontrada'}), status= 200, content_type="application_json")

@app.route('/edit/<int:id>', methods=['PUT', 'POST'])
def edit(id):
    estudante = Estudante.query.get(id)
    
    # Lógica para atualizar os dados
    estudante.nome = request.form['nome']
    estudante.idade = request.form['idade']

    # Realizar a confirmação 
    db.session.commit()

    # Lógica para processar a requisição POST
    return Response(response=json.dumps(estudante.to_dict()), status=200, content_type="application_json")



@app.route('/delete/<int:id>', methods=['GET', 'DELETE'])
def delete(id):
    estudante = Estudante.query.get(id)
    db.session.delete(estudante)
    db.session.commit()
    return Response(response=json.dumps(estudante.to_dict()), status=200, content_type="application_json")

