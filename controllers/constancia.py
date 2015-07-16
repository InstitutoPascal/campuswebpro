# coding: utf8

# intente algo como
response.title = "Campus Web Pro"

def alumno_regular():
    response.subtitle= "Constancia De Alumno Regular"
    q = db.alumnos.user_id== auth.user_id    #guardo en la consulta el registro del alumno
    alumno= db(q).select().first() #traemos el alumno para notificarlo en la vista
    return {'alumno': alumno}
    return {}


def materias_aprobadas(): 
    response.subtitle= "Certificado De Materias Aprobadas"
    q = db.alumnos.user_id== auth.user_id    #guardo en la consulta el registro del alumno
    alumno= db(q).select().first() #traemos el alumno para notificarlo en la vista
    return {'alumno': alumno}
    return {}

def titulo_en_tramite(): 
    response.subtitle= "Certificado De Titulo En Tramite"
    q = db.alumnos.user_id== auth.user_id    #guardo en la consulta el registro del alumno
    alumno= db(q).select().first() #traemos el alumno para notificarlo en la vista
    return {'alumno': alumno}
    return {}

def reincorporacion(): 
    response.subtitle= "Reincorporación De Alumno"
    q = db.alumnos.user_id== auth.user_id    #guardo en la consulta el registro del alumno
    alumno= db(q).select().first() #traemos el alumno para notificarlo en la vista
    return {'alumno': alumno}
    return {}
