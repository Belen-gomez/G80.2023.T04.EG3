"""
Tests OrderDelivery
"""
import json
import os
import unittest
from pathlib import Path
from unittest import TestCase
from freezegun import freeze_time
from uc3m_logistics import OrderManager
from uc3m_logistics import OrderManagementException

JSON_TEST_PATH = str(Path.home()) + "/PycharmProjects/G80.2023.T04.EG3/src/Json/tests/"
JSON_STORE_PATH = str(Path.home()) + "/PycharmProjects/G80.2023.T04.EG3/src/Json/store/"


class TestOrderDelivery(TestCase):
    """
    Tests OrderDelivery
    """
    #@freeze_time("2023-03-13")
    def test_ok(self):
        """
        test ok
        """
        myfile = OrderManager()

        #file_test = JSON_TEST_PATH + "test_ok.json"
        my_value = myfile.deliver_product("9626d1c11d0f544588ab0b5be51279b32e96c7d35b956b782d9d8f4b813ec867")
        self.assertEqual(my_value, True)

        file_store = JSON_STORE_PATH + "store_delivery.json"

        with (open(file_store, "r", encoding= "UTF-8", newline="")) as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item["Tracking_code"] == "9626d1c11d0f544588ab0b5be51279b32e96c7d35b956b782d9d8f4b813ec867":
                found = True
        self.assertTrue(found)
