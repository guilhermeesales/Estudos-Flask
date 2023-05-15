# Aula 9 - Templates
from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")


# Codificar criação de templates
@app.route("/")
def index():
    x = 50 
    y = 10
    query = dict(request.args)
    return render_template(f"index.html", x=x, y=y, query=query)



if __name__ == "__main__":
    app.run(debug=True)