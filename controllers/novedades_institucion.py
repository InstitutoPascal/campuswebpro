# -*- coding: utf-8 -*-
# intente algo como
def index(): return dict(message="Bienvenido a Novedades Institucionales")

@auth.requires_login()
@auth.requires_membership(role='Directivos')
def cargar_novedades():
    form=SQLFORM(db.novedades_institucion)
    if form.accepts(request.vars, session):
        response.flash = 'Cargado Correctamente'
    elif form.errors:
        response.flash = 'El Formulario contiene errores'
    else:
        response.flash = 'Por favor complete todos los campos del formulario'
    return dict(form=form)

def mostrar_novedades():
    response.title = "Novedades"
    response.subtitle="Novedades Institucionales"   
    
    i=0
    subtitulo=T('Novedades Instiucionales')#Asigna mensaje a mostrar
    novedades = db().select(db.novedades_institucion.ALL, distinct = True)
    for x in novedades:
        i=i+1
    lista=[]
    lista.append(TABLE(TR(TH('FECHA',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('TITULO',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('TEXTO',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('IMAGEN',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
    *[TR(TD(rows.fecha_novedad,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
    TD(rows.titulo,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(rows.texto,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(IMG(_src=URL(c='default',f='download',args=rows.imagen),_style='width:180px'),_style='width:280px; float: right; display: block'),_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd')
    for rows in novedades]),))
    tablaFinal = DIV(lista)
    return dict(subtitulo=subtitulo,t=tablaFinal)
