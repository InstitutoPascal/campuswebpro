
db.define_table('agenda_tipos',
    Field('agenda_tiposid', type='id'),
    Field('nombre', type='string', length=100),
    format= "%(agenda_tiposid)s [%(nombre)s]",
    migrate=True, fake_migrate=False)

db.define_table('agenda',
    Field('agendaid', type='id'),
    Field('fecha', type='date'),
    Field('profesorid', db.profesores),
    Field('materiaid', db.materias),
    Field('agenda_tiposid', db.agenda_tipos),
    Field('mensaje', type='string', length=200),
    migrate=True, fake_migrate=False)
