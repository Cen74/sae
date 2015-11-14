
from datetime import datetime
import sys
import os
from bottle import Bottle, route, run, template, request, get, post, view

import sae


app = Bottle()

@app.route('/')
def hello():
    return "Hello, world! - Bottle"


def diary_lines():
    diary = open('diary.txt')
    content = diary.readlines()
    content = content
    diary.close()
    return content 

def check_file():
    if os.path.exists('diary.txt'):
        file_content = diary_lines()
    else:
        file_content = "Empty Diary" 

    return file_content
    

def diary_write(data):  
    with open('diary.txt', 'a+') as diary:
        wtime = datetime.now()
        diary.write(wtime.strftime("%Y/%m/%d %H:%M:%S ")+ data) 
        diary.write('\n')


@app.get('/diary')
def welcome():
	data = check_file()
	return template('welcome_diary', content=data )

@app.post('/diary')
def print_input():
    client_input = request.forms.get('content')
 #   diary_write(client_input)
 #   data = diary_lines()
    return template('welcome_diary', content=client_input)

application = sae.create_wsgi_app(app)


'''
import sae

def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return ['Hello, world!']

application = sae.create_wsgi_app(app)

'''