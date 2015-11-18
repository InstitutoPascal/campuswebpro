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
    q &=db.inscripcionescarrera.carreraid==db.carreras.carreraid
    nombre=db(q).select(db.carreras.nombre,
                         db.carreras.carreraid,
                         db.inscripcionescarrera.carreraid)

    return dict (
                 alumno=alumno,
                 nombre=nombre
                 )
    
 


@auth.requires_membership(role='Alumnos')
#def actualizar():
    #response.subtitle= "Menú Actualizar Tramite"
    #s = db.alumnos.user_id== auth.user_id    #guardo en la consulta el registro del alumno
    #alumno= db(s).select().first() #traemos el alumno para notificarlo en la vista
    #s &=db.alumnos.alumnoid==db.inscripcionescarrera.alumnoid
    #s &=db.inscripcionescarrera.carreraid==db.carreras.carreraid
    #nombre=db(s).select(db.carreras.nombre,
      #                  db.carreras.carreraid,
     #                   db.inscripcionescarrera.carreraid)

    #return dict (nombre=nombre, alumno=alumno)
    

@auth.requires_membership(role='Alumnos')
def actualizar():
    response.subtitle= "Menú Actualizar Tramite"
    #q = db.alumnos.user_id== auth.user_id    #guardo en la consulta el registro del alumno
    #alumno= db(s).select().first() #traemos el alumno para notificarlo en la vista
    s = db.alumnos.user_id== auth.user_id    #guardo en la consulta el registro del alumno
    alumno= db(s).select().first() #traemos el alumno para notificarlo en la vista
    s &=db.alumnos.alumnoid==db.inscripcionescarrera.alumnoid
    s &=db.inscripcionescarrera.carreraid==db.carreras.carreraid
    nombre=db(s).select(db.carreras.nombre,
                        db.carreras.carreraid,
                        db.inscripcionescarrera.carreraid)

    
    q = db.tramites.tramiteid==db.expedientes.tramiteid
    q&= db.expedientes.estadoid==db.estados.estadoid
    lista=[]
    lista=db(q).select(db.tramites.tramiteid,
                       db.tramites.descripcion,
                       db.estados.descripcion)
    
    return dict (lista=lista, nombre=nombre, alumno=alumno)

@auth.requires_membership(role='Directivos')
def personal():
    response.subtitle= "Menú administrador tramite"
    q = db.personal.user_id== auth.user_id    #guardo en la consulta el registro del alumno
    personal= db(q).select().first() #traemos el alumno para notificarlo en la vista
    q = db.personal.personalid==db.personal.personalid
    nombre = db(q).select(db.personal.nombre)

    return dict (nombre=nombre, personal=personal)


@auth.requires_membership(role='Alumnos')
def alumno_regular():
    response.subtitle= "Constancia De Alumno Regular"
    q = db.alumnos.user_id== auth.user_id    #guardo en la consulta el registro del alumno
    alumno= db(q).select().first() #traemos el alumno para notificarlo en la vista
    q &=db.alumnos.alumnoid==db.inscripcionescarrera.alumnoid
    q &=db.inscripcionescarrera.carreraid==db.carreras.carreraid
    nombre=db(q).select(db.carreras.nombre,
                         db.carreras.carreraid,
                         db.inscripcionescarrera.carreraid)

    return dict (
                 alumno=alumno,
                 nombre=nombre
                 )

@auth.requires_membership(role='Alumnos')
def materias_aprobadas(): 
    response.subtitle= "Certificado De Materias Aprobadas"
    q = db.alumnos.user_id== auth.user_id    #guardo en la consulta el registro del alumno
    alumno= db(q).select().first() #traemos el alumno para notificarlo en la vista
    q &=db.alumnos.alumnoid==db.inscripcionescarrera.alumnoid
    q &=db.inscripcionescarrera.carreraid==db.carreras.carreraid
    nombre=db(q).select(db.carreras.nombre,
                         db.carreras.carreraid,
                         db.inscripcionescarrera.carreraid)

    return dict (
                 alumno=alumno,
                 nombre=nombre
                 )

@auth.requires_membership(role='Alumnos')
def titulo_en_tramite(): 
    response.subtitle= "Certificado De Titulo En Tramite"
    q = db.alumnos.user_id== auth.user_id    #guardo en la consulta el registro del alumno
    alumno= db(q).select().first() #traemos el alumno para notificarlo en la vista
    q &=db.alumnos.alumnoid==db.inscripcionescarrera.alumnoid
    q &=db.inscripcionescarrera.carreraid==db.carreras.carreraid
    nombre=db(q).select(db.carreras.nombre,
                         db.carreras.carreraid,
                         db.inscripcionescarrera.carreraid)

    return dict (
                 alumno=alumno,
                 nombre=nombre
                 )
    
    
@auth.requires_membership(role='Alumnos')
def reincorporacion(): 
    response.subtitle= "Reincorporación De Alumno"
    q = db.alumnos.user_id== auth.user_id    #guardo en la consulta el registro del alumno
    alumno= db(q).select().first() #traemos el alumno para notificarlo en la vista
    return {'alumno': alumno}
    return {}
