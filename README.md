wsgi-101
===============

Understanding wsgi. Task: 

* [x] Create urls.py in a separate module
* [x] Create views.py in a separate module

Error message: 

Traceback (most recent call last):
  File "/usr/lib/python2.7/wsgiref/handlers.py", line 85, in run
    self.result = application(self.environ, self.start_response)
  File "main.py", line 57, in application
    for regex, callback in urls:
TypeError: 'module' object is not iterable
127.0.0.1 - - [06/Nov/2014 18:13:53] "GET / HTTP/1.1" 500 59
Traceback (most recent call last):
  File "/usr/lib/python2.7/wsgiref/handlers.py", line 85, in run
    self.result = application(self.environ, self.start_response)
  File "main.py", line 57, in application
    for regex, callback in urls:
TypeError: 'module' object is not iterable
127.0.0.1 - - [06/Nov/2014 18:13:53] "GET /favicon.ico HTTP/1.1" 500 59

