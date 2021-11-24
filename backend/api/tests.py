from rest_framework.test import APISimpleTestCase
from .urls import Routes


class PrinterTest(APISimpleTestCase):
    def print_thing(self):
        print(f"{Routes = }")
