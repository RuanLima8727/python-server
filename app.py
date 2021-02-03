from flask import Flask, render_template, request

app = Flask(__name__, template_folder="./src/views")

@app.route("/", methods=["GET", "POST"])
def home():
    if (request.method == "GET"):
        return render_template("index.html")
    else:
       if(request.form["num1"] != "" and request.form["num2"] != ""):
            soma = int(request.form["num1"]) + int(request.form["num2"])
            return str(soma)
       else:
            return "Valores Invalidos"


@app.route("/teste<int:id>")
def parametroUrl(id):
    return str(id + 1)

@app.errorhandler(404)
def erroNotFound(error):
    return render_template("error.html")

@app.errorhandler(405)

def erroVerboErrado(error):
    return "Esse verbo não é aceito"


app.run(port=8080, debug=True)
