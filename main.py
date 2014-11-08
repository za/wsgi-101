#!/usr/bin/python

from cgi import parse_qs, escape
from wsgiref.simple_server import make_server
import re

# import your own created module
import views
import urls

def application(environ, start_response):
    """
    The main WSGI application. Dispatch the current request to
    the functions from above and store the regular expression
    captures in the WSGI environment as  `myapp.url_args` so that
    the functions from above can access the url placeholders.

    If nothing matches call the `not_found` function.
    """
    path = environ.get('PATH_INFO', '').lstrip('/')
    for regex, callback in urls.urls: 
	# so this for will check for two variable in urls.urls
	# urls datatype is tuple which has list 
	# urls = [(r'^$', views.index),(r'^hello/?$', views.hello)
	# the first one called regex and the other is the callback
        match = re.search(regex, path)	
		# match = re.search(pattern, string)
		# match datatype is boolean
        if match is not None:
		# so if this true
            environ['myapp.url_args'] = match.groups()
			# what's groups function?
			# and I think this environ 
			# and myapp.url_args is the keywords for 2nd exercise
            return callback(environ, start_response)
    return views.not_found(environ, start_response)

def main():
	
    srv = make_server('localhost', 8080, application)
    srv.serve_forever()

if __name__ == '__main__':
	main()
