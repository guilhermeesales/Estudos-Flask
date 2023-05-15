# Aula 10 Enviando dados para o template

from flask import Flask, render_template, request
from json import dumps

app = Flask(__name__, template_folder="templates")


#code
@app.route("/")
def notas():
    return render_template("index.html") 


@app.route("/resultado", methods=['POST', "GET"])
def resultado():
    total = dict(request.form)
    soma = str(sum([int(x) for x in total.values()]))
    return f"O total da soma é {soma}"


if __name__ == "__main__":
    app.run(debug=True)