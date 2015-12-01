
 # -*- coding: UTF-8 -*- 
#from datetime import datetime
#import sys
#import os
from bottle import Bottle, route, run, template, request, get, post, view, debug
import xml.etree.ElementTree as ET

import sae
import hashlib
#import sae.kvdb

#kv = sae.kvdb.Client()

app = Bottle()
debug(True)

application = sae.create_wsgi_app(app)


def check_signature():
    token = 'janet2mm'

    timestamp = request.query.timestamp
    nonce = request.query.nonce
    signature = request.query.signature
    echostr = request.query.echostr

    login_str = ''.join(sorted([token, timestamp, nonce]))
    check_login = hashlib.sha1(login_str).hexdigest()

    #print type(signature), type(check_login)
    #print "singnture:%s, check_login:%s" % (signature, check_login)

    if check_login == signature: # 如果是 if check_login is signature 就会报错, signature 是unicode object
        return echostr
    else: 
        return None


@app.get('/weixin')
def login():
    return check_signature()
   

@app.post('/exchange')
def test():
    print request.body.read()
    #print request.forms.keys()
    #str_xml = request.forms.keys()[0] # 只有第一个。
    #print str_xml[0]  
    
    #weixin_msg = ET.fromstring(str_xml)
    #print weixin_msg.tag, weixin_msg.attrib
    #print weixin_msg.findtext('Content')
    return ''   # 新浪认证后就ok  




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




