
from datetime import datetime
import sys
import os
from bottle import Bottle, route, run, template, request, get, post, view

import sae
import sae.kvdb

kv = sae.kvdb.Client()

app = Bottle()

@app.route('/')
def hello():
    return "Hello, world! - Bottle"


def diary_lines():
    content = [] 
    for i in kv.getkeys_by_prefix('Null'):
        content += [kv.get(i)]
    return content 


def check_file():
    keys = kv.getkeys_by_prefix('')
    if not keys:
        content = ['Empty Diary']
    else:
        content = diary_lines() 

    return content
    

def diary_write(data):  
    wtime = datetime.now()
    str_wtime = wtime.strftime("%Y-%m-%d-%H-%M-%S")

    key = 'Null:'+str_wtime
    kv.set(key, data)
   



@app.get('/diary')
def welcome():
    history = check_file()
    return template('welcome_diary', content = history)

@app.post('/diary')
def print_input():
    client_input = request.forms.get('content')
    diary_write(client_input)
    data = diary_lines()
    return template('welcome_diary', content=data)

@app.get('/cmd')
def log():
    history_cmd = check_file()
    return 'ok'


application = sae.create_wsgi_app(app)


