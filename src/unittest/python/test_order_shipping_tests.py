import json
import os
import unittest
from pathlib import Path
from unittest import TestCase
from freezegun import freeze_time
from uc3m_logistics import OrderManager
from uc3m_logistics import OrderManagementException

JSON_TEST_PATH = "C:/Users/ferna/Desktop/Desarrollodesoftware/G80.2023.T04.EG3/src/Json/tests/"
class TestOrderShipping(TestCase):

    @freeze_time("2023-03-13")
    def test_ok(self):
        myfile = OrderManager()

        file_test = JSON_TEST_PATH +"test_ok.json"
        my_value= myfile.send_product(file_test)
        self.assertEqual(my_value, "hffuudujdjkf")

        file_store = JSON_TEST_PATH + "store_shipping.json"

        with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item["_OrderShipping__order_id"] == "39c990e813534575b3a114b44a38f08a":
                found = True
        self.assertTrue(found)

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

    def test_2_deletion(self):
        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            file = myfile.send_product(JSON_TEST_PATH + "test_2_deletion.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        file_store = JSON_TEST_PATH + "store_shipping.json"
        found = False
        creado = True
        try:
            with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
                data_list = json.load(file)
        except FileNotFoundError as ex:
            creado = False
        if not found and creado:
            for item in data_list:
                if item["_OrderShipping__order_id"] == "39c990e813534575b3a114b44a38f08a":
                    found = True

        self.assertFalse(found)

    def test_2_duplication(self):
        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            file = myfile.send_product(JSON_TEST_PATH + "test_2_double.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)
