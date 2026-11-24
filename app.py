from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
@app.get("/login")
def login():
    return render_template("login.html")


@app.get("/register")
def register():
    return render_template("register.html")

# Paciente

@app.get("/paciente")
def paciente_inicio():
    return render_template("paciente/inicio.html")


@app.get("/paciente/servicios")
def paciente_servicios():
    return render_template("paciente/servicios.html")


@app.get("/paciente/citas/nueva")
def paciente_solicitar_cita():
    return render_template("paciente/solicitar_cita.html")


@app.get("/paciente/citas")
def paciente_citas():
    return render_template("paciente/citas.html")


@app.get("/paciente/citas/historial")
def paciente_historial_citas():
    return render_template("paciente/historial_citas.html")


@app.get("/paciente/tratamientos")
def paciente_tratamientos():
    return render_template("paciente/tratamientos.html")


@app.get("/paciente/perfil")
def paciente_perfil():
    return render_template("paciente/perfil.html")

