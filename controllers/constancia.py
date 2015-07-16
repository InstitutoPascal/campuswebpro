# coding: utf8
# intente algo como
def alumno_regular():
    q = db.alumnos.user_id== auth.user_id    #guardo en la consulta el registro del alumno
    alumno= db(q).select().first() #traemos el alumno para notificarlo en la vista
    return {'alumno': alumno}
    return {}


def materias_aprobadas(): 
    q = db.alumnos.user_id== auth.user_id    #guardo en la consulta el registro del alumno
    alumno= db(q).select().first() #traemos el alumno para notificarlo en la vista
    return {'alumno': alumno}
    return {}

def titulo_en_tramite(): 
    q = db.alumnos.user_id== auth.user_id    #guardo en la consulta el registro del alumno
    alumno= db(q).select().first() #traemos el alumno para notificarlo en la vista
    return {'alumno': alumno}
    return {}

def reincorporacion(): 
    q = db.alumnos.user_id== auth.user_id    #guardo en la consulta el registro del alumno
    alumno= db(q).select().first() #traemos el alumno para notificarlo en la vista
    return {'alumno': alumno}
  

def alumno_regular2(): 
    return {}

def materias_aprobadas2(): 
    return {}

def titulo_en_tramite2(): 
    return {}

def reincorporacion2(): 
    return {}
