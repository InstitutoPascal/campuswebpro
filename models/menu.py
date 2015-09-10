# -*- coding: utf-8 -*- 

T.force("es")

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.title = request.application
#response.subtitle = T('customize me!')

##########################################
## this is the main application menu
## add/remove items as required
##########################################

response.menu = [
    [T('Alumnos'), False, URL(request.application,'alumnos','index'), ],
       
    [T('Docentes'), False, URL(request.application,'docentes','index'),],
    [T('Plantel Docente'), False, URL(request.application,'info','plantel_docente'), []],
[T('Historia'), False, URL(request.application,'info','historia'), []],
    [T('Cartelera'), False, URL(request.application,'cartelera','menu'), [
       # [T('Por que elegirnos'), False, URL(request.application,'info','por_que_elegirnos'),[]],              
             # [T('Palabras del Director'), False, URL(request.application,'info','director'), []],
       # [T('Cartelera'), False, URL(request.application,'cartelera','menu'), []]
    ]],
    [T('Carreras'), False, URL(request.application,'carreras','index')],


            
    

    
    
    [T('Tramites'), False, URL(request.application,'tramites','index'), [
       [T('Iniciar'), False, URL(request.application,'tramites','iniciar'), []],
 #       [T('Consultar'), False, URL(request.application,'tramites','consultar'),[]],
        [T('Actualizar'), False, URL(request.application,'tramites','actualizar',),[]],
#    [T('Constancias'), False, URL(request.application,'default','index'), [ 
 #       [T('Alumno Regular'), False, URL(request.application,'constancia','alumno_regular'), []],
  #     [T('Titulo en Tramite'), False, URL(request.application,'constancia','titulo_en_tramite'), []],
   #    [T('Reincorporacion'), False, URL(request.application,'constancia','reincorporacion'), []],
    #   [T('Materias Aprobadas'), False, URL(request.application,'constancia','materias_aprobadas'), []],
   ]],   


    [T('Novedades'), False, URL(request.application,'novedades_institucion','mostrar_novedades'), []],
    
    [T('Admin'), False, "https://www.institutopascal.edu.ar/admin", []],
    ]
