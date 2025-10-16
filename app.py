from flask import Flask, render_template, request, redirect, url

app.config['secret']

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/animales")
def animales():
    return render_template("animales.html")

@app.route("/vehiculos")
def carros():
    return render_template("vehiculos.html")

@app.route("/maravillas")
def maravillas():
    return render_template("maravillas.html")

@app.route("/acerca")
def acerca():
    return render_template("acerca.html")

@app.route("/formulario" , method = ("GET, POST"))
def inicio():
    return render_template("formulario.html")
error=None
if request.method == "POST":
    Nombre = request.form ["Nombre"]
    Apellido = request.form ["Apellido"]
    Fecha = request.form ["Fecha"]
    Genero = request.form ["Genero"]
    Numero = request.form ["Numero"]
    Contra = request.form ["Contra"]
    
    if Contra != ContraConfirm:
        error = "La contraseña no coincide"
        if error != None:
            flash(error)
            return render_template("formulario.html")
        else:
            flash(f"Registro exitoso para el usuario:{Nombre, Apellido}")
            return render_template ("inicio.html")

@app.route("/sesion")
def inicio():
    return render_template("sesion.html")


if __name__ == "__main__":
    app.run(debug=True)