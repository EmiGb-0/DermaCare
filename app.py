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

#Dermatologo 
@app.get("/dermatologo")
def dermatologo_dashboard():
    return render_template("dermatologo/dashboard.html")

@app.get("/dermatologo/citas")
def dermatologo_citas():
    return render_template("dermatologo/citas.html")

@app.get("/dermatologo/pacientes")
def dermatologo_pacientes():
    return render_template("dermatologo/pacientes.html")

@app.get("/dermatologo/historial")
def dermatologo_historial():
    return render_template("dermatologo/historial.html")

@app.get("/dermatologo/consulta")
def dermatologo_consulta():
    return render_template("dermatologo/consulta.html")

@app.get("/dermatologo/diagnosticos")
def dermatologo_diagnosticos():
    return render_template("dermatologo/diagnosticos.html")

@app.get("/dermatologo/seguimiento")
def dermatologo_seguimiento():
    return render_template("dermatologo/seguimiento.html")

# Administrador
@app.get("/administrador")
def administrador_dashboard():
    return render_template("administrador/dashboard.html")


@app.get("/administrador/usuarios")
def administrador_usuarios():
    return render_template("administrador/usuarios.html")


@app.get("/administrador/pacientes")
def administrador_pacientes():
    return render_template("administrador/pacientes.html")


@app.get("/administrador/dermatologos")
def administrador_dermatologos():
    return render_template("administrador/dermatologos.html")


@app.get("/administrador/citas")
def administrador_citas():
    return render_template("administrador/citas.html")


@app.get("/administrador/servicios")
def administrador_servicios():
    return render_template("administrador/servicios.html")


@app.get("/administrador/reportes")
def administrador_reportes():
    return render_template("administrador/reportes.html")


@app.get("/administrador/configuracion")
def administrador_configuracion():
    return render_template("administrador/configuracion.html")

