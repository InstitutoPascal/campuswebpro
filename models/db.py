# -*- coding: utf-8 -*-
###########################################################
DESARROLLO = False
if request.vars.lang: session.lang=request.vars.lang
T.force("es")

T.current_languages=['es','es-ar','es-es']
###################################################

if request.env.web2py_runtime_gae:            # if running on Google App Engine
    db = DAL('gae')                           # connect to Google BigTable
    session.connect(request, response, db=db) # and store sessions and tickets there
    ### or use the following lines to store sessions in Memcache
    # from gluon.contrib.memdb import MEMDB
    # from google.appengine.api.memcache import Client
    # session.connect(request, response, db=MEMDB(Client())
elif DESARROLLO:                                         # else use a normal relational database
    db = DAL('sqlite://storage.sqlite')       # if not, use SQLite or other DB
else:
    db = DAL(DB_URI, pool_size=10)
    ## if no need for session
# session.forget()

#########################################################################
## Here is sample code if you need for 
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - crud actions
## comment/uncomment as needed
#from gluon.tools import Auth, Crud, Service, PluginManager, prettydate
#auth = Auth(db)
#crud, service, plugins = Crud(db), Service(), PluginManager()


from gluon.tools import *
auth=Auth(globals(),db)                      # authentication/authorization
auth.settings.hmac_key='sha512:b13de948-def0-4fd4-baf6-bef3f83b5d88'
auth.settings.create_user_groups=None
auth.define_tables(migrate=MIGRATE, fake_migrate=FAKE_MIGRATE)                         # creates all needed tables
crud=Crud(globals(),db)                      # for CRUD helpers using auth
service=Service(globals())                   # for json, xml, jsonrpc, xmlrpc, amfrpc

crud.settings.auth=auth                      # enforces authorization on crud

# -*- coding: utf-8 -*- 

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
#########################################################################


# crud.settings.auth=auth                      # enforces authorization on crud
mail=Mail()                                  # mailer
mail.settings.server='localhost:25'    # your SMTP server
mail.settings.sender='info@institutopascal.edu.ar'         # your email
mail.settings.login='username:password'      # your credentials or None
auth.settings.mailer=mail                    # for user email verification
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.messages.verify_email = 'Presione en el enlace http://'+request.env.http_host+URL(r=request,c='default',f='user',args=['verify_email'])+'/%(key)s para verificar su cuenta de correo electrónico.'

#auth.messages.Confirm_Password = 'Verificar Contraseña'
auth.messages.verify_password = 'Verificar Contraseña'
auth.messages.label_remember_me = 'Recordarme (30 dias)'
auth.messages.verify_password_comment = 'Ingrese su contraseña nuevamente'
auth.messages.register_button = 'Registrarse'
auth.messages.login_button = 'Iniciar sesión'

auth.settings.reset_password_requires_verification = True
auth.messages.reset_password = 'Presione en el enlace http://'+request.env.http_host+URL(r=request,c='default',f='user',args=['reset_password'])+'/%(key)s para reestablecer su contraseña'

##from gluon.tools import Recaptcha 
##auth.settings.captcha = Recaptcha(request, '6Lc7kAcAAAAAABrrdJW9yOiqugkPI_gW-XhV2Ieo',  '6Lc7kAcAAAAAADN2Mj9KT56LjpXFr5-tEj9j2yWo')

## more options discussed in gluon/tools.py
#########################################################################

#########################################################################
## Define your tables below, for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################
