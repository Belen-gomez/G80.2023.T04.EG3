import json
import os
import unittest
from pathlib import Path
from unittest import TestCase
from freezegun import freeze_time
from uc3m_logistics import OrderManager
from uc3m_logistics import OrderManagementException


class TestOrderShipping(TestCase):

    def test_wrong_file_not_found(self):
        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            file = myfile.send_product("abu")
        self.assertEqual("Archivo no encontrado", cm.exception.message)

    def test_wrong_file_not_JSON(self):
        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            file = myfile.send_product("C:/Users/nacho/PycharmProjects/G80.2023.T04.EG3/src/main/python/uc3m_logistics/order_manager.py")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)