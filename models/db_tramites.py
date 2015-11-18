##db = DAL("postgres://reingart:clave@localhost:5432/terciario", pool_size=10)

migrate = True

db.define_table('tramites',
    Field('tramiteid', type='id'),
    Field('descripcion', type='string',default=""),
#    Field('arancelado', type='boolean', default=False),
    format= "%(tramiteid)s [%(descripcion)s]",
    migrate=MIGRATE, fake_migrate=FAKE_MIGRATE)


#db.define_table('ubicaciones',
#    Field('ubicacionid', type='id'),
#    Field('descripcion', type='string', default=""),
#    Field('telefono', type='string', default=""),
#    Field('email', type='string', default=""),
#    format= "%(ubicacionid)s [%(descripcion)s]",
#    migrate=MIGRATE, fake_migrate=FAKE_MIGRATE)

    
db.define_table('estados',
    Field('estadoid', type='id'),
    Field('descripcion', type='string', default=""),
    Field('activo', type='boolean', default=False),
    format= "%(estadoid)s [%(descripcion)s]",
    migrate=MIGRATE, fake_migrate=FAKE_MIGRATE)

    
db.define_table('expedientes',
    Field('expedienteid', type='id'),
    Field("alumnoid", db.alumnos),
    Field('tramiteid', db.tramites),
    Field('estadoid', db.estados),
    Field("mensaje", "text"),
    format= "%(expedienteid)s [%(mensaje)s]",
    migrate=MIGRATE, fake_migrate=FAKE_MIGRATE)


#db.define_table("seguimientos",
#    Field('seguimientoid', type='id'),
#    Field("expedienteid", db.expedientes),
#    Field("personalid", db.personal),  # directivo
#    Field("ubicacionid", db.ubicaciones),
#    Field('fecha', type='date', length=200,label=T('Fecha')),
#    Field("comentario", "text"),
#    format= "%(seguimientoid)s [%(comentario)s]",
#    migrate=MIGRATE, fake_migrate=FAKE_MIGRATE)
