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
    CICLOID=5 #ciclo lectivo 2014
    #q=db.materias.cursoid==ANIO
    q=db.asignaturas.carreraid==CARRERAID
    q&=db.asignaturas.cicloid==CICLOID
    q&=db.asignaturas.materiaid==db.materias.materiaid
    q&=db.materias.materiaid==db.comisiones.materiaid
    q&=db.comisiones.comisionid==db.horarios.comisionid
    q&=db.horarios.horaid==db.horas.horaid
    q&=db.comisiones.personalid==db.personal.personalid
    filas=db(q).select(db.materias.nombre,db.horarios.dia,db.horas.desde,db.horas.hasta,db.personal.nombre,db.materias.cursoid)
    cursos ={}
    return {'filas':filas}



def agenda():
    response.title = "cartelera"
    response.subtitle="agenda"
    # muestra un perfil personalizado del alumno.
    q = db.alumnos.user_id== auth.user_id  
     # obtengo el registro del alumno ya registrado como usuario 
    alumno= db(q).select( db.alumnos.nombre,
                         db.alumnos.fechanacimiento,
                         db.alumnos.estadocivil,
                         db.alumnos.foto,
                         db.alumnos.email1,
                         db.alumnos.ingreso,
                         db.alumnos.localidad,
                         db.alumnos.nacionalidad,
                         db.alumnos.alumnoid).first()
    q &= db.inscripcionescomision.alumnoid== db.alumnos.alumnoid
    q &= db.inscripcionescomision.comisionid== db.comisiones.comisionid
    q &= db.comisiones.materiaid== db.materias.materiaid
    q &= db.comisiones.divisionid== db.divisiones.divisionid
    q &= db.divisiones.cicloid== db.ciclos.cicloid
    q &= db.materias.materiaid== db.asignaturas.materiaid
    q &= db.asignaturas.carreraid== db.carreras.carreraid
    datos= db(q).select(db.comisiones.nombre,
                        db.inscripcionescomision.alta,
                        db.ciclos.anio,
                        db.carreras.nombre)
    inscripcion= db(db.inscripcionescomision).select(db.inscripcionescomision.alumnoid,
                                                     db.inscripcionescomision.comisionid)
    #envio todos los alumnos y comisiones para luego comparar en ficha.
    alumnos= db(db.alumnos).select(db.alumnos.user_id,
                                   db.alumnos.alumnoid)
    return dict (alumno=alumno, dato=datos,
                 inscripcion=inscripcion)
     
    

def examenes():
    response.title = "Cartelera"
    response.subtitle="Exámenes Finales"
    CARRERAID=1 #analisis de sistemas
    CICLOID=5 #ciclo lectivo 2014
    LLAMADO=1 #PRIMER LLAMADO
    EXAMEN_PERIODO=30 #EXAMEN DICIEMBRE 2014
    COMISION_PERIODO=33 #periodo2014

    q=db.asignaturas.carreraid==CARRERAID
    q&=db.asignaturas.cicloid==CICLOID
    q&=db.materias.materiaid==db.asignaturas.materiaid #OBTENEMOS COD Y NOMBRE DE MATERIA
    q&=db.cursos.cursoid==db.materias.cursoid #OBTENEMOS EL NOMBRE DEL CURSO
    #OBTENEMOS EL EXAMEN DE ESA MATERIA EN EL PERIODO DICIEMBRE 2014 Y EL PRIMER LLAMADO
    q&=db.materias.materiaid==db.examenes.materiaid
    q&=db.examenes.periodoid==EXAMEN_PERIODO
    q&=db.examenes.llamado==LLAMADO 
    #OBTENGO LA MATERIA CORRELATIVA DE LA ACTUAL
    q&=db.materias.materiaid==db.correlativas.materiaid
    #CONSULTAMOS COMISION ACTUAL DE LA MATERIA EN ESTE PERIODO 2014 PARA VER EL DOCENTE
    q&=db.materias.materiaid==db.comisiones.materiaid
    q&=db.comisiones.periodoid==COMISION_PERIODO
    q&=db.comisiones.personalid==db.personal.personalid
    filas=db(q).select(db.materias.codigo,db.materias.nombre,db.cursos.nombre, db.examenes.fecha,db.examenes.hora,db.correlativas.materiacorrelativa,db.personal.nombre)
    correla_map ={}
    for fila in filas:
        MATERIA=fila.correlativas.materiacorrelativa
        q=db.materias.materiaid==MATERIA
        materias=db(q).select(db.materias.codigo)
        for materia in materias:
            if fila.materias.codigo==materia.codigo: #SI EL COD DE MATERIA = COD DE CORRELA
                correla_map[fila.materias.codigo] = '---'
            else:
                correla_map[fila.materias.codigo] = materia.codigo
    return {'filas':filas,'correla_map':correla_map}
