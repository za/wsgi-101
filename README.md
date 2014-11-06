wsgi-101
===============

Understanding wsgi. Task: 

* [x] Create urls.py in a separate module
* [x] Create views.py in a separate module

still found errors

```python
Traceback (most recent call last):
  File "/usr/lib/python2.7/wsgiref/handlers.py", line 85, in run
    self.result = application(self.environ, self.start_response)
  File "main.py", line 23, in application
    return callback(environ, start_response)
  File "/home/za/dev/github/marimore/django-tutorial/views.py", line 15, in hello
    subject = escape(args[0])
NameError: global name 'escape' is not defined
127.0.0.1 - - [06/Nov/2014 23:53:48] "GET /hello/daf HTTP/1.1" 500 59
Traceback (most recent call last):
  File "/usr/lib/python2.7/wsgiref/handlers.py", line 85, in run
    self.result = application(self.environ, self.start_response)
  File "main.py", line 24, in application
    return views(not_found(environ, start_response))
NameError: global name 'not_found' is not defined
```

Errors solved.
