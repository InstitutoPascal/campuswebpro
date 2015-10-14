# coding: utf8
# try something like
response.title= "Campus Web Pro"


def index(): return plugin_flatpage()


@auth.requires_membership(role='Alumnos')
def iniciar():
    response.subtitle= "Menú Iniciar Tramite"
    q = db.alumnos.user_id== auth.user_id    #guardo en la consulta el registro del alumno
    alumno= db(q).select().first() #traemos el alumno para notificarlo en la vista
    q &=db.alumnos.alumnoid==db.inscripcionescarrera.alumnoid
    #carrera=db(q &) .inscripcionescarrera.carreraid==db.carreras.nombre
    return {'alumno': alumno}


@auth.requires_membership(role='Alumnos')
def actualizar():
    response.subtitle= "Menú Actualizar Tramite"
    s = db.alumnos.user_id== auth.user_id    #guardo en la consulta el registro del alumno
    alumno= db(s).select().first() #traemos el alumno para notificarlo en la vista
    return {'alumno': alumno}
