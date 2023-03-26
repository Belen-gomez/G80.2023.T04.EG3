"""
Tests order_shipping
"""
import json
import unittest
from pathlib import Path
from unittest import TestCase
from freezegun import freeze_time
from uc3m_logistics import OrderManager
from uc3m_logistics import OrderManagementException


JSON_FILE_PATH = str(Path.home()) + "/PycharmProjects/G80.2023.T04.EG3/src/Json/store/"


class TestOrderManager(TestCase):
    """
    Tests order_shipping
    """

    @freeze_time("2023-02-19")
    def test_correct_complete_regular(self):
        """
        test ok
        """
        my_order = OrderManager()
        my_value = my_order.register_order(product_id="8421691423220", address="C/LISBOA,4, MADRID, SPAIN",
                                           zip_code="28005", phone="123456789", order_type="REGULAR")
        self.assertEqual(my_value, "39c990e813534575b3a114b44a38f08a")

        file_store = JSON_FILE_PATH + "store_request.json"

        with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item["_OrderRequest__order_id"] == "39c990e813534575b3a114b44a38f08a":
                found = True
        self.assertTrue(found)

    @freeze_time("2023-02-19")
    def test_correct_complete_premium(self):
        """
        test ok
        """
        my_order = OrderManager()
        my_value = my_order.register_order(product_id="8421691423220", address="C/LISBOA,4, MADRID, SPAIN",
                                           zip_code="28005", phone="123456789", order_type="PREMIUM")
        self.assertEqual(my_value, "834d88b261c0af0f337546cf73448809")

        file_store = JSON_FILE_PATH + "store_request.json"

        with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item["_OrderRequest__order_id"] == "834d88b261c0af0f337546cf73448809":
                found = True
        self.assertTrue(found)

    def test_with_product_code_wrong_string(self):
        """
        test wrong
        """
        my_order = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            my_order.register_order("842169142322A", "C/LISBOA,4, MADRID, SPAIN", "PREMIUM", "123456789",
            "28005")
        self.assertEqual("Invalid EAN13 code string", cm.exception.message)

        file_store = JSON_FILE_PATH + "store_request.json"
        found = False
        creado = True
        try:
            with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
                data_list = json.load(file)
        except FileNotFoundError:
            creado = False
        if not found and creado:
            for item in data_list:
                if item["_OrderRequest__product_id"] == "842169142322A":
                    found = True
        self.assertFalse(found)

    def test_with_product_code_wrong_sum(self):
        """
        test wrong
        """
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.register_order("8421691423225", "C/LISBOA,4, MADRID, SPAIN", "PREMIUM", "123456789",
                                            "28005")
        self.assertEqual("Invalid EAN13 code sum", cm.exception.message)

        file_store = JSON_FILE_PATH + "store_request.json"
        found = False
        creado = True
        try:
            with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
                data_list = json.load(file)
        except FileNotFoundError:
            creado = False
        if not found and creado:
            for item in data_list:
                if item["_OrderRequest__product_id"] == "8421691423225":
                    found = True
        self.assertFalse(found)

    def test_with_product_code_wrong_len12(self):
        """
        test wrong
        """
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.register_order("842169142322", "C/LISBOA,4, MADRID, SPAIN", "REGULAR", "123456789",
                                            "28005")
        self.assertEqual("Invalid EAN13 code len < 13", cm.exception.message)

        file_store = JSON_FILE_PATH + "store_request.json"
        found = False
        creado = True
        try:
            with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
                data_list = json.load(file)
        except FileNotFoundError:
            creado = False
        if not found and creado:
            for item in data_list:
                if item["_OrderRequest__product_id"] == "842169142322":
                    found = True
        self.assertFalse(found)

    def test_with_product_code_wrong_len14(self):
        """
        test wrong
        """
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.register_order("84216914232200", "C/LISBOA,4, MADRID, SPAIN", "REGULAR", "123456789",
                                            "28005")
        self.assertEqual("Invalid EAN13 code len > 13", cm.exception.message)

        file_store = JSON_FILE_PATH + "store_request.json"
        found = False
        creado = True
        try:
            with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
                data_list = json.load(file)
        except FileNotFoundError:
            creado = False
        if not found and creado:
            for item in data_list:
                if item["_OrderRequest__product_id"] == "84216914232200":
                    found = True
        self.assertFalse(found)

    def test_with_order_type_wrong(self):
        """
        test wrong
        """
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.register_order("8421691423220", "C/LISBOA,4, MADRID, SPAIN", "PRE", "123456789",
                                            "28005")
        self.assertEqual("Order type wrong", cm.exception.message)

        file_store = JSON_FILE_PATH + "store_request.json"
        found = False
        creado = True
        try:
            with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
                data_list = json.load(file)
        except FileNotFoundError:
            creado = False
        if not found and creado:
            for item in data_list:
                if item["_OrderRequest__order_type"] == "PRE":
                    found = True
        self.assertFalse(found)

    def test_with_address_short(self):
        """
        test wrong
        """
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.register_order("8421691423220", "C/LISBOA,4, MADRID,", "PREMIUM",  "123456789",
                                            "28005")
        self.assertEqual("Address too short", cm.exception.message)

        file_store = JSON_FILE_PATH + "store_request.json"
        found = False
        creado = True
        try:
            with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
                data_list = json.load(file)
        except FileNotFoundError:
            creado = False
        if not found and creado:
            for item in data_list:
                if item["_OrderRequest__delivery_address"] == "C/LISBOA,4, MADRID":
                    found = True
        self.assertFalse(found)

    def test_with_address_long(self):
        """
        test wrong
        """
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.register_order("8421691423220", "C/LISBOA,4, MADRID, SPAIN SPAINSPAINSPAINSPAINSPAINSPAINSPAINSPAINSPAINSPAINSPAINSPAINSPAINSPAINSPAIN",
                                    "REGULAR", "123456789", "28005")
        self.assertEqual("Address too long", cm.exception.message)

        file_store = JSON_FILE_PATH + "store_request.json"
        found = False
        creado = True
        try:
            with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
                data_list = json.load(file)
        except FileNotFoundError:
            creado = False
        if not found and creado:
            for item in data_list:
                if item["_OrderRequest__delivery_address"] == "C/LISBOA,4, MADRID, SPAIN SPAINSPAINSPAINSPAINSPAINSPAINSPAINSPAINSPAINSPAINSPAINSPAINSPAINSPAINSPAIN":
                    found = True
        self.assertFalse(found)

    def test_with_address_wrong(self):
        """
        test wrong
        """
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.register_order("8421691423220", "C/LISBOA,4,MADRID,SPAIN", "REGULAR", "123456789",
                                            "28005")
        self.assertEqual("Direccion sin espacios", cm.exception.message)

        file_store = JSON_FILE_PATH + "store_request.json"
        found = False
        creado = True
        try:
            with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
                data_list = json.load(file)
        except FileNotFoundError:
            creado = False
        if not found and creado:
            for item in data_list:
                if item["_OrderRequest__delivery_address"] == "C/LISBOA,4,MADRID,SPAIN":
                    found = True
        self.assertFalse(found)

    def test_with_phone_str(self):
        """
        test wrong
        """
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.register_order("8421691423220", "C/LISBOA,4, MADRID, SPAIN", "REGULAR", "12345A789",
                                            "28005")
        self.assertEqual("Phone number is a string", cm.exception.message)

        file_store = JSON_FILE_PATH + "store_request.json"
        found = False
        creado = True
        try:
            with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
                data_list = json.load(file)
        except FileNotFoundError:
            creado = False
        if not found and creado:
            for item in data_list:
                if item["_OrderRequest__phone_number"] == "12345A789":
                    found = True
        self.assertFalse(found)

    def test_with_phone_short(self):
        """
        test wrong
        """
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.register_order("8421691423220",  "C/LISBOA,4, MADRID, SPAIN", "REGULAR", "12345678",
                                            "28005")
        self.assertEqual("Phone number too short", cm.exception.message)

        file_store = JSON_FILE_PATH + "store_request.json"
        found = False
        creado = True
        try:
            with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
                data_list = json.load(file)
        except FileNotFoundError:
            creado = False
        if not found and creado:
            for item in data_list:
                if item["_OrderRequest__phone_number"] == "12345678":
                    found = True
        self.assertFalse(found)

    def test_with_phone_long(self):
        """
        test wrong
        """
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.register_order("8421691423220", "C/LISBOA,4, MADRID, SPAIN", "REGULAR", "1234567890",
                                            "28005")
        self.assertEqual("Phone number too long", cm.exception.message)

        file_store = JSON_FILE_PATH + "store_request.json"
        found = False
        creado = True
        try:
            with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
                data_list = json.load(file)
        except FileNotFoundError:
            creado = False
        if not found and creado:
            for item in data_list:
                if item["_OrderRequest__phone_number"] == "1234567890":
                    found = True
        self.assertFalse(found)

    def test_with_zip_code_not_valid(self):
        """
        test wrong
        """
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.register_order("8421691423220", "C/LISBOA,4, MADRID, SPAIN", "REGULAR", "123456789",
                                            "67008")
        self.assertEqual("Zip code is not valid", cm.exception.message)

        file_store = JSON_FILE_PATH + "store_request.json"
        found = False
        creado = True
        try:
            with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
                data_list = json.load(file)
        except FileNotFoundError:
            creado = False
        if not found and creado:
            for item in data_list:
                if item["_OrderRequest__zip_code"] == "67008":
                    found = True
        self.assertFalse(found)

    def test_with_zip_code_str(self):
        """
        test wrong
        """
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.register_order("8421691423220", "C/LISBOA,4, MADRID, SPAIN", "REGULAR", "123456789",
                                            "280A8")
        self.assertEqual("Zip code is a string", cm.exception.message)

        file_store = JSON_FILE_PATH + "store_request.json"
        found = False
        creado = True
        try:
            with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
                data_list = json.load(file)
        except FileNotFoundError:
            creado = False
        if not found and creado:
            for item in data_list:
                if item["_OrderRequest__zip_code"] == "280A8":
                    found = True
        self.assertFalse(found)

    def test_with_zip_code_short(self):
        """
        test wrong
        """
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.register_order("8421691423220", "C/LISBOA,4, MADRID, SPAIN", "REGULAR", "123456789",
                                            "2800")
        self.assertEqual("Zip code too short", cm.exception.message)

        file_store = JSON_FILE_PATH + "store_request.json"
        found = False
        creado = True
        try:
            with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
                data_list = json.load(file)
        except FileNotFoundError:
            creado = False
        if not found and creado:
            for item in data_list:
                if item["_OrderRequest__zip_code"] == "2800":
                    found = True
        self.assertFalse(found)

    def test_with_zip_code_long(self):
        """
        test wrong
        """
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.register_order("8421691423220", "C/LISBOA,4, MADRID, SPAIN", "REGULAR", "123456789",
                                            "280055")
        self.assertEqual("Zip code too long", cm.exception.message)

        file_store = JSON_FILE_PATH + "store_request.json"
        found = False
        creado = True
        try:
            with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
                data_list = json.load(file)
        except FileNotFoundError:
            creado = False
        if not found and creado:
            for item in data_list:
                if item["_OrderRequest__zip_code"] == "280055":
                    found = True
        self.assertFalse(found)


if __name__ == '__main__':
    unittest.main()
