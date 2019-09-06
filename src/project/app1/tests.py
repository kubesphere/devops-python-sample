# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client


class MyClassTestCase(TestCase):
    def SetUp(self):
        pass

    def test_my_func(self):
        print('[OK] Test running')


class MyAppTests(TestCase):
    def setUp(self):
        super(MyAppTests, self).setUp()
        self.client = Client(enforce_csrf_checks=True)

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
