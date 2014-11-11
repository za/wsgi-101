#!/usr/bin/python

from cgi import parse_qs, escape
import re

import something.views
import settings

import importlib

root_urlconf = importlib.import_module(settings.ROOT_URLCONF)

def application(environ, start_response):
    """
    The main WSGI application. Dispatch the current request to
    the functions from above and store the regular expression
    captures in the WSGI environment as  `myapp.url_args` so that
    the functions from above can access the url placeholders.

    If nothing matches call the `not_found` function.
    """
    path = environ.get('PATH_INFO', '').lstrip('/')
    
    for regex, callback in root_urlconf.urlpatterns: 
        match = re.search(regex, path)	
        if match is not None:
            environ['myapp.url_args'] = match.groups()
            return callback(environ, start_response)
    return something.views.not_found(environ, start_response)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8080, application)
    srv.serve_forever()
