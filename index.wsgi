
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
'''  

def check_file():
    if os.path.exists('diary.txt'):
        file_content = diary_lines()
    else:
        file_content = "Empty Diary" 

    return file_content
    
'''
def diary_write(data):  
    wtime = datetime.now()
    str_wtime = wtime.strftime("%Y-%m-%d-%H-%M-%S")

    key = 'Null:'+str_wtime
    kv.set(key, data)
   



@app.get('/diary')
def welcome():
    return template('welcome_diary', content = [])

@app.post('/diary')
def print_input():
    client_input = request.forms.get('content')
    diary_write(client_input)
    data = diary_lines()
    return template('welcome_diary', content=data)


application = sae.create_wsgi_app(app)


