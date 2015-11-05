# coding: utf8
# try something like
def index():
    q=db.carreras.carreraid>0
    carreras=db(q).select()
    return{'carreras':carreras}

def materias():
    carreraid=request.args[0]
    q= db.asignaturas.carreraid==carreraid
    q &= db.asignaturas.carreraid==db.carreras.carreraid
    q &= db.asignaturas.materiaid==db.materias.materiaid
    q &= db.asignaturas.cursoid==db.cursos.cursoid
    q &= db.comisiones.materiaid==db.materias.materiaid
    #q &= db.profesores.comisionid==db.comisiones.comisionid
    q &= db.personal.personalid==db.comisiones.personalid

    filas=db(q).select(db.materias.nombre, db.materias.codigo, db.personal.nombre)
    return{'filas': filas}

def sistemas():
    return {}

def salud():
    return {}

def salud_enfermeria():
    return {}

def salud_cardiologia():
    return {}

def salud_laboratorio():
    return {}

def salud_auxenfermeria():
    return {}

def salud_instrumentacion():
    return {}

def salud_radiologia():
    return {}

def redes():
    return {}
    
def programas():
    
    return{}

def horarios():
    return{}

def metodologia():
    return {}

def teleinformatica():
    return {}

def practica():
    return {}

def programacion():
    return {}
