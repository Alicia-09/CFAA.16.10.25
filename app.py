from flask import Flask, render_template, request, redirect, flash, url_for, session

app = Flask(__name__)
USUARIOS_REGISTRADOS = {
    "24308060610613@cetis61.edu.mx"
        "Nombre": "Ali",
        "Apellido": "Campos",
        "Contra": "Ali091903."
}

app.config['SECRET_KEY'] = 'Ali091903'

@app.route("/")
def inicio():
    
    if 'usuario_email' not in session:
        flash('Por favor inicia sesión primero', 'error')
        return redirect(url_for('login'))
    
    usuario = USUARIOS_REGISTRADOS[session['usuario_email']]
    return render_template("inicio.html", usuario=usuario)

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

@app.route("/formulario" , methods = ["GET", "POST"])
def formulario():

    error=None
    if request.method == "POST":
        Nombre = request.form["Nombre"]
        Apellido = request.form["Apellido"]
        Fecha = request.form["Fecha"]
        Genero = request.form["Genero"]
        Email = request.form["Email"]
        Contra = request.form["Contra"]
        ContraConfirm = request.form["ContraConfirm"]
    
        if Contra != ContraConfirm:
            error = "La contraseña no coincide"
            if error != None:
                flash(error)
            return render_template("formulario.html")
        else:
            USUARIOS_REGISTRADOS[Email] = {
                "Nombre": Nombre,
                "Apellido": Apellido,
                "Contra": Contra
            }

            
            flash(f"Registro exitoso para el usuario:{Nombre} {Apellido}")
            return redirect (url_for ("login"))

    return render_template("formulario.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@app.route('/ValidaSesion', methods=['GET', 'POST'])
def ValidaSesion():
    if request.method == "POST":
        Email = request.form.get('Email', '').strip()
        Contra = request.form.get('Contra', '')
        
        if not Email or not Contra:
            flash('Por favor ingresa email y contraseña','error')
        elif Email in USUARIOS_REGISTRADOS:
            usuario = USUARIOS_REGISTRADOS[Email]
            if usuario['Contra'] == Contra:
                session['usuario_email'] = Email
                session['usuario'] = usuario['Nombre']
                session['logueado'] = True
                return redirect(url_for('inicio'))
            
        else:
            flash('Contraseña incorrecta','error')
    else:
        flash('usuario no encontrado','error')
        
if __name__ == "__main__":
    app.run(debug=True)