# coding: utf8
# intente algo como
def index(): return dict(message="hello from cartelera.py")
def menu():
    response.title = "cartelera"
   
    
    return {}
   
    
def horarios():
    response.title = "Cartelera"
    response.subtitle="Horarios de las materias"
    CARRERAID=1 #analisis de sistemas
    ANIO=1 #PRIMER AÑO
    CICLOID=6 #ciclo lectivo 2015
    #q=db.materias.cursoid==ANIO
    q=db.asignaturas.carreraid==CARRERAID
    q&=db.asignaturas.cicloid==CICLOID
    q&=db.asignaturas.materiaid==db.materias.materiaid
    q&=db.materias.materiaid==db.comisiones.materiaid
    q&=db.comisiones.comisionid==db.horarios.comisionid
    q&=db.horarios.horaid==db.horas.horaid
    q&=db.comisiones.personalid==db.personal.personalid
    filas=db(q).select(db.horarios.horarioid,db.materias.nombre,db.horarios.dia,db.horas.desde,db.horas.hasta,db.personal.nombre,db.materias.cursoid)
    sql = db._lastsql
    return {'filas':filas, "sql": sql}
def editar_horarios():
    HORARIOID = request.args[0]
    form = SQLFORM(db.horarios, HORARIOID)
    if form.accepts(request.vars, session):
        session.flash = "OK!"
        redirect(URL(f="horarios"))
    elif form.errors:
        response.flash = "Corrija los errores!"
    else:
        response.flash = "complete el formulario"
    return {"form": form}
def agregar_horarios():
    form = SQLFORM(db.horarios)
    if form.accepts(request.vars, session):
        session.flash = "OK!"
        redirect(URL(f="horarios"))
    elif form.errors:
        response.flash = "Corrija los errores!"
    else:
        response.flash = "complete el formulario"
    return {"form": form}
        
def agenda():
   response.title = "cartelera"
   response.subtitle="Agenda"   
   response.subtitle= "Inscripcion Carrera"
   form = SQLFORM.factory(
        Field("Date", "date"),
        
        )
   if form.process().validate:
    response.flash = form.vars.Date
   return dict (form=form)
    


def examenes():
    response.title = "Cartelera"
    response.subtitle="Exámenes Finales"   
    
    CARRERAID=1 #analisis de sistemas
    CICLOID=6 #ciclo lectivo 2015
    LLAMADO=1 #PRIMER LLAMADO
    EXAMEN_PERIODO=35 #EXAMEN DICIEMBRE 2014
    COMISION_PERIODO=33 #periodo2014
    
    q=db.asignaturas.carreraid==CARRERAID
    q&=db.asignaturas.cicloid==CICLOID
    q&=db.materias.materiaid==db.asignaturas.materiaid #OBTENEMOS COD Y NOMBRE DE MATERIA
    q&=db.cursos.cursoid==db.materias.cursoid #OBTENEMOS EL NOMBRE DEL CURSO
    #OBTENEMOS EL EXAMEN DE ESA MATERIA EN EL PERIODO DICIEMBRE 2014 Y EL PRIMER LLAMADO
    q&=db.materias.materiaid==db.examenes.materiaid
    q&=db.examenes.periodoid==EXAMEN_PERIODO
    ##q&=db.examenes.llamado==LLAMADO 
    #OBTENGO LA MATERIA CORRELATIVA DE LA ACTUAL
    ###q&=db.materias.materiaid==db.correlativas.materiaid
    #CONSULTAMOS COMISION ACTUAL DE LA MATERIA EN ESTE PERIODO 2014 PARA VER EL DOCENTE
    ##q&=db.materias.materiaid==db.comisiones.materiaid
    ##q&=db.comisiones.periodoid==COMISION_PERIODO
    ##q&=db.comisiones.personalid==db.personal.personalid
    q&=db.examenes.personalid1==db.personal.personalid
    filas=db(q).select(db.examenes.examenid, db.materias.materiaid, db.materias.codigo,db.materias.nombre,db.cursos.nombre, db.examenes.fecha,db.examenes.hora,db.personal.nombre)
    sql = db._lastsql
    correla_map ={}
    for fila in filas:
        MATERIAID=fila.materias.materiaid
        q=db.correlativas.materiaid==MATERIAID
        q&=db.materias.materiaid==db.correlativas.materiacorrelativa
        correlativas=db(q).select(db.materias.codigo)
        correla_map[fila.materias.codigo] = []  # lista de correlativas
        for correlativa in correlativas:
            correla_map[fila.materias.codigo].append(correlativa.codigo)
    return {'filas':filas,'correla_map':correla_map, "sql": sql}


def editar_examen():
    EXAMENID = request.args[0]
    
    form = SQLFORM(db.examenes, EXAMENID)
    if form.accepts(request.vars, session):
        session.flash = "OK!"
        redirect(URL(f="examenes"))
    elif form.errors:
        response.flash = "Corrija los errores!"
    else:
        response.flash = "complete el formulario"
    return {"form": form}

def agregar_examen():
    form = SQLFORM(db.examenes)
    if form.accepts(request.vars, session):
        session.flash = "OK!"
        redirect(URL(f="examenes"))
    elif form.errors:
        response.flash = "Corrija los errores!"
    else:
        response.flash = "complete el formulario"
    return {"form": form}
