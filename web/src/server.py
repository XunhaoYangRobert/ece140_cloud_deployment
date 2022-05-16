from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.renderers import render_to_response

import mysql.connector as mysql
import os

db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']
db_host = os.environ['MYSQL_HOST']

def get_home(req):
  # Connect to the database and retrieve the users
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("select first_name, last_name, email from Users;")
  records = cursor.fetchall()
  db.close()

  return render_to_response('templates/home.html', {'users': records}, request=req)

def get_product(req):
   # Connect to the database and retrieve the users
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("select first_name, last_name, email from Users;")
  records = cursor.fetchall()
  db.close()

  return render_to_response('templates/product.html', {'users': records}, request=req)

def get_kvp(req):
  
   db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
   cursor = db.cursor()
   cursor.execute("select first_name, last_name, email from Users;")
   records = cursor.fetchall()
   db.close()

   return render_to_response('templates/kvp.html', {'users': records}, request=req)

def get_UI(req):
  
   db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
   cursor = db.cursor()
   cursor.execute("select first_name, last_name, email from Users;")
   records = cursor.fetchall()
   db.close()

   return render_to_response('templates/UI.html', {'users': records}, request=req)   

def get_laws(req):
  
   db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
   cursor = db.cursor()
   cursor.execute("select first_name, last_name, email from Users;")
   records = cursor.fetchall()
   db.close()

   return render_to_response('templates/laws.html', {'users': records}, request=req)

def get_IA(req):
  
   db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
   cursor = db.cursor()
   cursor.execute("select first_name, last_name, email from Users;")
   records = cursor.fetchall()
   db.close()

   return render_to_response('templates/IA.html', {'users': records}, request=req)    

def get_UX(req):
  
   db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
   cursor = db.cursor()
   cursor.execute("select first_name, last_name, email from Users;")
   records = cursor.fetchall()
   db.close()

   return render_to_response('templates/UX.html', {'users': records}, request=req)    

''' Route Configurations '''
if __name__ == '__main__':
  config = Configurator()

  config.include('pyramid_jinja2')
  config.add_jinja2_renderer('.html')

  config.add_route('get_home', '/')
  config.add_view(get_home, route_name='get_home')

  config.add_route('get_product', '/product')
  config.add_view(get_product, route_name='get_product')

  config.add_route('get_kvp', '/kvp')
  config.add_view(get_kvp, route_name='get_kvp')

  config.add_route('get_UI', '/UI')
  config.add_view(get_UI, route_name='get_UI')

  config.add_route('get_laws', '/laws')
  config.add_view(get_laws, route_name='get_laws')

  config.add_route('get_IA', '/IA')
  config.add_view(get_IA, route_name='get_IA')

  config.add_route('get_UX', '/UX')
  config.add_view(get_UX, route_name='get_UX')

  config.add_static_view(name='/', path='./public', cache_max_age=3600)

  app = config.make_wsgi_app()
  server = make_server('0.0.0.0', 6000, app)
  server.serve_forever()