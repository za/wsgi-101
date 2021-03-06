#!/usr/bin/python

import unittest

from main import application

def start_response(*args, **kwargs):
    pass

class TestApplication(unittest.TestCase):
    def test_root_path(self):
        environ = {
            'PATH_INFO' : '/',
        }

        response = application(environ, start_response)
        self.assertTrue('Hello World Application' in "".join(response))

    def test_hello_zaki(self):
        environ = {
            'PATH_INFO' : '/hello/zaki',
        }

        response = application(environ, start_response)
        self.assertTrue('Hello zaki' in "".join(response))

    def test_not_found(self):
        environ = {
            'PATH_INFO' : '/something',
        }

        response = application(environ, start_response)
        self.assertTrue('Not Found' in "".join(response))


if __name__ == '__main__':
    unittest.main()
