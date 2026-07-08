from flask import Flask, render_template, request

app = Flask(__name__)

def converter(valor, origem, destino):

    if origem == destino:
        return valor

    if origem == "C":
        if destino == "F":
            return (valor * 9/5) + 32
        if destino == "K":
            return valor + 273.15

    if origem == "F":
        if destino == "C":
            return (valor - 32) * 5/9
        if destino == "K":
            return (valor - 32) * 5/9 + 273.15

    if origem == "K":
        if destino == "C":
            return valor - 273.15
        if destino == "F":
            return (valor - 273.15) * 9/5 + 32

    return valor


@app.route("/", methods=["GET", "POST"])
def home():

    resultado = None

    if request.method == "POST":
        valor = float(request.form["valor"])
        origem = request.form["origem"]
        destino = request.form["destino"]

        resultado = round(converter(valor, origem, destino), 2)

    return render_template("index.html", resultado=resultado)


if __name__ == "__main__":
    app.run(debug=True)