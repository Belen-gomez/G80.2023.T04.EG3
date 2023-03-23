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

class TestOrderShipping(TestCase):

    @freeze_time("2023-03-13")
    def test_ok(self):
        """
        test ok
        """
        myfile = OrderManager()

        file_test = JSON_TEST_PATH +"test_ok.json"
        my_value= myfile.send_product(file_test)
        self.assertEqual(my_value, "9626d1c11d0f544588ab0b5be51279b32e96c7d35b956b782d9d8f4b813ec867")

        file_store = JSON_STORE_PATH + "store_shipping.json"

        with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item["_OrderShipping__order_id"] == "39c990e813534575b3a114b44a38f08a":
                found = True
        self.assertTrue(found)

    def test_wrong_file_not_found(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)
        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            file = myfile.send_product("abu")
        self.assertEqual("Archivo no encontrado", cm.exception.message)
        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_wrong_alamcen_not_found(self):
        pass

    def test_wrong_pedido_no_encontrado(self):
        pass
    def test_wrong_file_not_JSON(self):
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            file = myfile.send_product(JSON_TEST_PATH + "test_no_json.txt")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_2_deletion(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            file = myfile.send_product(JSON_TEST_PATH + "test_2_deletion.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_2_duplication(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            file = myfile.send_product(JSON_TEST_PATH + "test_2_duplication.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_3_deletion(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            file = myfile.send_product(JSON_TEST_PATH + "test_3_deletion.json")
        self.assertEqual("Pedido vacío", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_3_duplication(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            file = myfile.send_product(JSON_TEST_PATH + "test_3_duplication.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_4_deletion(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            file = myfile.send_product(JSON_TEST_PATH + "test_4_deletion.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_4_duplication(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            file = myfile.send_product(JSON_TEST_PATH + "test_4_duplication.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_5_modification(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            file = myfile.send_product(JSON_TEST_PATH + "test_5_modification.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_6_duplication(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            file = myfile.send_product(JSON_TEST_PATH + "test_6_duplication.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_6_deletion(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            file = myfile.send_product(JSON_TEST_PATH + "test_4_deletion.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_7_duplication(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            file = myfile.send_product(JSON_TEST_PATH + "test_7_duplication.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_7_deletion(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            file = myfile.send_product(JSON_TEST_PATH + "test_7_deletion.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_8_duplication(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            file = myfile.send_product(JSON_TEST_PATH + "test_8_duplication.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_8_deletion(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            file = myfile.send_product(JSON_TEST_PATH + "test_8_deletion.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_9_modification(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            file = myfile.send_product(JSON_TEST_PATH + "test_9_modification.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_10_deletion(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            file = myfile.send_product(JSON_TEST_PATH + "test_10_deletion.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_10_duplication(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            file = myfile.send_product(JSON_TEST_PATH + "test_10_duplication.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_11_deletion(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            file = myfile.send_product(JSON_TEST_PATH + "test_11_duplication.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_11_duplication(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            file = myfile.send_product(JSON_TEST_PATH + "test_11_duplication.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_12_deletion(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            file = myfile.send_product(JSON_TEST_PATH + "test_12_duplication.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_12_duplication(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            file = myfile.send_product(JSON_TEST_PATH + "test_12_duplication.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_13_modification(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            file = myfile.send_product(JSON_TEST_PATH + "test_13_modification.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_14_deletion(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            file = myfile.send_product(JSON_TEST_PATH + "test_11_duplication.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_14_duplication(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            file = myfile.send_product(JSON_TEST_PATH + "test_14_duplication.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_15_deletion(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            file = myfile.send_product(JSON_TEST_PATH + "test_15_duplication.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_15_duplication(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            file = myfile.send_product(JSON_TEST_PATH + "test_15_duplication.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_16_deletion(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            file = myfile.send_product(JSON_TEST_PATH + "test_16_duplication.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_16_duplication(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            file = myfile.send_product(JSON_TEST_PATH + "test_16_duplication.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_17_deletion(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            file = myfile.send_product(JSON_TEST_PATH + "test_17_duplication.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_17_duplication(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            file = myfile.send_product(JSON_TEST_PATH + "test_17_duplication.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_18_deletion(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            file = myfile.send_product(JSON_TEST_PATH + "test_18_duplication.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_18_duplication(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            file = myfile.send_product(JSON_TEST_PATH + "test_18_duplication.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_19_deletion(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            file = myfile.send_product(JSON_TEST_PATH + "test_19_duplication.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_19_duplication(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            file = myfile.send_product(JSON_TEST_PATH + "test_19_duplication.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")