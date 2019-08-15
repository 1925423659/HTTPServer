from wsgiref.simple_server import make_server
import requests
import urllib
import json

def application(environ, start_response):
    for key, values in environ.items():
        print(key, ' -> ', values)
    request_method = environ['REQUEST_METHOD']
    if request_method == 'GET':
        return application_get(environ, start_response)
    if request_method == 'POST':
        return application_post(environ, start_response)

def application_get(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/json')])
    return [response(environ, 'get')]

def application_post(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/json')])
    return [response(environ, 'post')]

def response(environ, response_method):
    print('<response begin>')
    query = urllib.parse.parse_qs(environ['QUERY_STRING'])
    content_length = 0
    if len(environ['CONTENT_LENGTH']) > 0:
        content_length = int(environ['CONTENT_LENGTH'])
    print('content_length', content_length)
    wsgi_input = environ['wsgi.input'].read(content_length)
    print('wsgi_input', wsgi_input)
    wsgi_input = str(wsgi_input, 'utf-8')
    print('wsgi_input', wsgi_input)
    data = {'response_method': response_method,
            'request_method': environ['REQUEST_METHOD'],
            'path_info': environ['PATH_INFO'],
            'query_string': environ['QUERY_STRING'],
            'query': query,
            'wsgi.input': wsgi_input}
    print(data)
    data = json.dumps(data)
    data = bytes(data, encoding='utf-8')
    print('<response end>')
    return data


httpd = make_server('', 8000, application)
httpd.serve_forever()