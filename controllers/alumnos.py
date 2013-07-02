# coding: utf8
# try something like

def busqueda():
    # armo un formulario para buscar alumno por su dni
    form = SQLFORM.factory(
        Field("dni", "integer"),
        Field("nombre", "string"),
        )
    q= db.alumnos.id>0
    if form.accepts(request.vars, session):
        # buscar el alumno
        q = db.alumnos.dni == form.vars.dni
        q&= db.alumnos.nombre == form.vars.nombre
        alumno = db(q).select().first()
        if alumno:
            # encontrado, redirigo a cargar notas por 
            redirect(URL(f=index, vars={'alumnoid': alumno.alumnoid}))
        else:
            response.flash = "Alumno no encontrado"
    #response.view = "generic.html"  # HACER una vista de verdad
    return dict (form = form)

def index(): 
    "menu alumno"
    return {}

def horarios():
    q= db.horarios.horaid==db.horas.horaid
    q &= db.horarios.comisionid== db.comisiones.comisionid
    q &= db.comisiones.personalid== db.personal.personalid
    q &= db.comisiones.materiaid== db.materias.materiaid
    filas= db(q).select(db.horas.hora, db.personal.nombre, db.materias.nombre, db.horarios.dia)
    
    horarios={'lunes':{},'martes':{},'miercoles':{},'jueves':{},'viernes':{}}
    for fila in filas:
        horarios[fila.dia][fila.hora]=fila
        
    return dict (filas= filas)
    
   
        
    
def inasistencias():
    q= db.faltas()
    q &= db.faltas.inasistenciaid== db.inasistencias.inasistenciaid
    q &= db.faltas.alumnoid== db.alumnos.alumnoid
    q &= db.faltas.comisionid== db.comisiones.comisionid
    faltas= db(q).select(db.alumno.nombre, db.comision.nombre)
    
    
    return {'falta', 'faltas'}
    
def examenes():
    "Listado de Examenes finales Rendi"
    return {}
    
def final():
    "formulario inscripcion a examen finales aptos para el alumno"
    return {}
    
def parciales():
    "listado de examenes cuatrimestrales rendidos"
    return{}
def inscripciones():
    "Listado de inscripciones"
    return {}
    
def archivos():
    "descarga de archivos pedagogicos subidos por docentes"
    return {}
