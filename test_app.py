import unittest
from flask import Flask
from flask_testing import TestCase
from app import app, generate_pswd_fibr, generate_pswd_dsl

class TestApp(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_generate_pswd_fibr(self):
        pswd = generate_pswd_fibr("00:11:22:33:44:55")
        self.assertEqual(pswd, "PLDTWIFI00:11:22:33:44:55")

    def test_generate_pswd_dsl(self):
        pswd = generate_pswd_dsl(123)
        self.assertEqual(pswd, "PLDTWIFI369")

    def test_pldt_mac(self):
        response = self.client.get('/mac/00:11:22:33:44:55')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['mac'], "001122334455")
        self.assertEqual(data['password'], "PLDTWIFI00112")

    def test_pldt_fibr(self):
        response = self.client.get('/fibr/PLDTFIBR_00112')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['ssid'], "PLDTFIBR_00112")
        self.assertEqual(data['password'], "PLDTWIFI00112")

    def test_pldt_dsl(self):
        response = self.client.get('/dsl/PLDTDSL_369')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['ssid'], "PLDTDSL_369")
        self.assertEqual(data['password'], "PLDTWIFI369")

if __name__ == '__main__':
    unittest.main()
