#!/usr/bin/python

from cgi import parse_qs, escape

def index(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html')]
    start_response(status, response_headers)
    return ['''Hello World Application

               This is the Hello World application:

               `continue <hello/>`_

            ''']

def hello(environ, start_response):
    args = environ['myapp.url_args']
    if args:
        subject = escape(args[0])
    else:
        subject = 'World'
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html')]
    start_response(status, response_headers)
    return ['''Hello %(subject)s
           
             Hello %(subject)s!

            ''' % {'subject': subject}]

def not_found(environ, start_response):
    status = '404 NOT FOUND'
    response_headers = [('Content-Type', 'text/plain')]
    start_response(status, response_headers)
    return ['Not Found']
