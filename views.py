#!/usr/bin/python

from cgi import parse_qs, escape

def index(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
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
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ['''Hello %(subject)s
           
             Hello %(subject)s!

            ''' % {'subject': subject}]

def not_found(environ, start_response):
    start_response('404 NOT FOUND', [('Content-Type', 'text/plain')])
    return ['Not Found']
