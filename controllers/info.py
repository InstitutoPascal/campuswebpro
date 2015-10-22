# coding: utf8
# try http://127.0.0.1:8000/admin/default/edit/campuswebpro/controllers/info.py?id=controllers__info__py#something like
def index(): return plugin_flatpage()

def historia():
    
   return plugin_flatpage()
   
 

def por_que_elegirnos():
   response.title = "plantel docente"
   response.subtitle="info"   


   i=0
   subtitulo=T('Plantel Docente ')#Asigna mensaje a mostrar
   personal = db().select(db.personal.ALL, distinct = True)
   for x in personal:
        i=i+1
        lista=[]
        lista.append(TABLE(TR(TH('Nombre',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Dni',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Localidad',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Foto',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),
    *[TR(TD(rows.nombre,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
    TD(rows.localidad,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(rows.dni,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(IMG(_src=URL(c='default',f='download',args=rows.foto),_style='width:180px'),_style='width:280px; float: right; display: block'),_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd')
    for rows in personal]),))
        tablaFinal = DIV(lista)
    
        return dict(subtitulo=subtitulo,t=tablaFinal)

  

def plantel_docente():
          
    filas=db(db.personal.personalid>0).select(db.personal.dni,db.personal.nombre,db.personal.dni,db.personal.foto)
        
    return {'filas':filas}

def director(): return plugin_flatpage()
