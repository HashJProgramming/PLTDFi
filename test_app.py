import unittest
from flask import Flask
from flask_testing import TestCase
from app import app, generate_pswd_fibr, generate_pswd_dsl

class TestApp(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_generate_pswd_fibr(self):
        pswd = generate_pswd_fibr('PLDTHOMEFIBRb4870'[-5:])
        print(pswd)
        pass

    def test_generate_pswd_dsl(self):
        pswd = generate_pswd_dsl('PLDTHOMEDSL12345'[-5:])
        print(pswd)
        pass
    
if __name__ == '__main__':
    unittest.main()
