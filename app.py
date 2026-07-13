from flask import Flask, render_template, request

app = Flask(__name__)
CELSIUS = "C"
FAHRENHEIT = "F"
KELVIN = "K"

def converter(valor, origem, destino):

    if origem == destino:
        return valor

    if origem == CELSIUS:
        if destino == FAHRENHEIT:
            return (valor * 9/5) + 32
        if destino == KELVIN:
            return valor + 273.15

    if origem == FAHRENHEIT:
        if destino == CELSIUS:
            return (valor - 32) * 5/9
        if destino == KELVIN:
            return (valor - 32) * 5/9 + 273.15

    if origem == KELVIN:
        if destino == CELSIUS:
            return valor - 273.15
        if destino == FAHRENHEIT:
            return (valor - 273.15) * 9/5 + 32

    return valor


@app.route("/", methods=["GET", "POST"])
def home():

    resultado = None

    erro = None

    if request.method == "POST":
        try:
            valor = float(request.form["valor"])
            origem = request.form["origem"]
            destino = request.form["destino"]

            resultado = round(converter(valor, origem, destino), 2)

        except ValueError:
            erro = "Digite um número válido."

    return render_template("index.html", resultado=resultado, erro=erro)


if __name__ == "__main__":
    app.run(debug=True)
