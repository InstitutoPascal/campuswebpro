# coding: utf8
# try something like
def index(): return plugin_flatpage()

def historia(): return plugin_flatpage()
def por_que_elegirnos(): return plugin_flatpage()
def plantel_docente():
    filas=db(db.personal.personalid>0).select(db.personal.dni,db.personal.nombre,db.personal.dni)
  
    return {'filas':filas}

def director(): return plugin_flatpage()
