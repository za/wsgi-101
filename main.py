from cgi import parse_qs, escape
from wsgiref.simple_server import make_server

import re
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
        match = re.search(regex, path)
        if match is not None:
            environ['myapp.url_args'] = match.groups()
            return callback(environ, start_response)
    return views.not_found(environ, start_response)

def main():
	
    srv = make_server('localhost', 8080, application)
    srv.serve_forever()

if __name__ == '__main__':
	main()
