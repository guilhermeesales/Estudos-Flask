# Aula 7 - Objetos de requisição

from flask import Flask, request
from json import dumps

app = Flask(__name__)


@app.route("/", methods={"GET", "POST"})
def init():
    print(request.method, request.args)
    t1 = request.args.to_dict()
    t2 = dict(request.args)  # Converter para dicionários
    return dumps([t1,t2])



if __name__ == '__main__':
    app.run(debug=True)

