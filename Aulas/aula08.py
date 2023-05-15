# Aula 08 - Redirecionando Erros
from flask import Flask, request, abort, redirect, url_for

app = Flask(__name__, static_folder="static")

# code

@app.route('/sucesso/')
def sucesso():
    return "Você entrou com sucesso na sua conta, parabéns!"


@app.route('/login/', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # code
        if request.form['username'] == "admin" and request.form['pswr'] == 'admin':
            return redirect(url_for("sucesso"), code=200)
        
        else:
            return 'Houve algum erro ao entrar no sistema'
    else:
        abort(403)  # Mostrar status de erros, 403 Proibido


if __name__ == "__main__":
    app.run(debug=True)