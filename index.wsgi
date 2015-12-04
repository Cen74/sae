
from datetime import datetime
import os
from bottle import Bottle, route, run, template, request, get, post, view, debug

import sys
#import os
# sys.setdefaultencoding() does not exist, here!import sys
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

import sae
import sae.kvdb

kv = sae.kvdb.Client()

app = Bottle()
debug(True)



@app.route('/')
def hello():
    return "Hello, world! - Bottle"

count = 0

def cli_write_diary(post):
    global count 
    count += 1

    wtime = datetime.now()
    str_wtime = wtime.strftime("%Y-%m-%d %H:%M:%S")

    key   = 'Key' + str(count)
    value =  {'time':str_wtime, 'content':post}
    kv.set(key, value)
    #for item in kv.get_by_prefix('Key'):
    #   print item[1], item[0]

def getkey(item):
    return item[0]

def cli_return_all():
    raw_kv = [ item for item in kv.get_by_prefix('Key') ]
    # 以
    sorted_kv = sorted(raw_kv, key=lambda x:x[0], reverse=True)
    result = [elment[1] for elment in sorted_kv]
    return result


@app.get('/newdiary')
def welcome():
    history = cli_return_all()
    return template('diary2', content = history)

@app.route('/newdiary', method='POST')
def print_input():
    client_input = request.forms.get('input')
    cli_write_diary(client_input)
    return template('diary2', content=cli_return_all())


application = sae.create_wsgi_app(app)












'''

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
    

def diary_write(data, TAG='Null'):  
    wtime = datetime.now()
    str_wtime = wtime.strftime("%Y-%m-%d-%H-%M-%S")

    key = TAG+':'+str_wtime
    kv.set(key, data)

    return "key:%s, value:%s" % (key, data)
   
def cmd_output(TAG='Null'):
    str_bytes = "Diary History:\n"
    key = TAG+':' 
    print 'TAG as:%s' % TAG
    str_bytes += 'TAG as:%s\n' % TAG

    if check_file() == 'Empty Diary':
        return 'Empty Diary'


    print kv.getkeys_by_prefix(key)
    for i in kv.getkeys_by_prefix(key):
        print kv.get(i)
        str_bytes += kv.get(i)
        str_bytes += '\n' 

    return str_bytes


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
def login():  
    return cmd_output()

@app.post('/cmd/set')
def set_tag():
    key = request.forms.get('key')
    kv.set(key, '')
    return 'set TAG:%s' % key

@app.post('/cmd/input')
def input_kv():
    key = request.forms.get('key')
    value = request.forms.get('value')
    return diary_write(value, key)

@app.post('/cmd/history')
def feedback_history():
    key = request.forms.get('key')  
    return cmd_output(key)   #'list' object has no attribute 'getkeys_by_prefix'

'''
