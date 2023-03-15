import os
import unittest
from unittest import TestCase
from freezegun import freeze_time
from uc3m_logistics import OrderManager
from uc3m_logistics import OrderManagementException

class TestOrderManager(TestCase):

    @freeze_time("2023-02-19")
    def test_correct_complete(self):
        file_store = JSON_FILES_PATH + "store_order_request.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_order = OrderManager()
        my_value = my_order.register_order(product_id="8421691423220", address="C/LISBOA,4, MADRID, SPAIN",
                                           zip_code="28005", phone="123456789", order_type="REGULAR")
        self.assertEqual(my_value, "6f651f23a6af8d79e5a30276d136b1ee")

        with (open(file_store, 'r', encoding="UTF-8",newline='')) as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item["_OrderRequest__order_id"] == "6f651f23a6af8d79e5a30276d136b1ee":
                found = True
        self.assertTrue(found)

    def test_with_product_code_wrong_string(self):
        my_order = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            value = my_order.register_order("842169142322A", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN", "123456789",
                                            "28005")
            self.assertEqual("Invalid EAN13 code string", cm.exception.message)

    def test_with_product_code_wrong_sum(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            value = my_order.register_order("8421691423225", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN", "123456789",
                                            "28005")
            self.assertEqual("Invalid EAN13 code sum", cm.exception.message)

    def test_with_product_code_wrong_len12(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            value = my_order.register_order("842169142322", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "123456789",
                                            "28005")
            self.assertEqual("Invalid EAN13 code len <13", cm.exception.message)

    def test_with_product_code_wrong_len14(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            value = my_order.register_order("84216914232200", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "123456789",
                                            "28005")
            self.assertEqual("Invalid EAN13 code len >13", cm.exception.message)

    def test_with_order_type_wrong(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            value = my_order.register_order("8421691423220", "PRE", "C/LISBOA,4, MADRID, SPAIN", "123456789",
                                            "28005")
            self.assertEqual("Order type wrong", cm.exception.message)

    def test_with_address_short(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            value = my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID,", "123456789",
                                            "28005")
            self.assertEqual("Address too short", cm.exception.message)

    def test_with_address_long(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            value = my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN SPAINSPAINSPAINSPAINSPAINSPAINSPAINSPAINSPAINSPAINSPAINSPAINSPAINSPAINSPAIN", "123456789",
                                            "28005")
            self.assertEqual("Address too long", cm.exception.message)

    def test_with_address_wrong(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            value = my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4,MADRID,SPAIN", "123456789",
                                            "28005")
            self.assertEqual("Direccion sin espacios", cm.exception.message)


if __name__ == '__main__':
    unittest.main()
