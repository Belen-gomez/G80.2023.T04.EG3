"""
Tests RF2
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

class TestOrderShipping(TestCase):
    """
    Tests RF2
    """
    @freeze_time("2023-03-13")
    def test_ok(self):
        """
        test ok
        """
        myfile = OrderManager()

        file_test = JSON_TEST_PATH + "test_ok.json"
        my_value = myfile.send_product(file_test)
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
            myfile.send_product("abu")
        self.assertEqual("Archivo no encontrado", cm.exception.message)
        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_wrong_alamcen_not_found(self):
        pass

    def test_wrong_pedido_no_encontrado(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_pedido_no_encontrado.json")
        self.assertEqual("El pedido no se encontró entre los pedidos registrados", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_wrong_file_not_json(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_no_json.txt")
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
            myfile.send_product(JSON_TEST_PATH + "test_2_deletion.json")
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
            myfile.send_product(JSON_TEST_PATH + "test_2_duplication.json")
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
            myfile.send_product(JSON_TEST_PATH + "test_3_deletion.json")
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
            myfile.send_product(JSON_TEST_PATH + "test_3_duplication.json")
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
            myfile.send_product(JSON_TEST_PATH + "test_4_deletion.json")
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
            myfile.send_product(JSON_TEST_PATH + "test_4_duplication.json")
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
            myfile.send_product(JSON_TEST_PATH + "test_5_modification.json")
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
            myfile.send_product(JSON_TEST_PATH + "test_6_duplication.json")
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
            myfile.send_product(JSON_TEST_PATH + "test_4_deletion.json")
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
            myfile.send_product(JSON_TEST_PATH + "test_7_duplication.json")
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
            myfile.send_product(JSON_TEST_PATH + "test_7_deletion.json")
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
            myfile.send_product(JSON_TEST_PATH + "test_8_duplication.json")
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
            myfile.send_product(JSON_TEST_PATH + "test_8_deletion.json")
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
            myfile.send_product(JSON_TEST_PATH + "test_9_modification.json")
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
            myfile.send_product(JSON_TEST_PATH + "test_10_deletion.json")
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
            myfile.send_product(JSON_TEST_PATH + "test_10_duplication.json")
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
            myfile.send_product(JSON_TEST_PATH + "test_11_deletion.json")
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
            myfile.send_product(JSON_TEST_PATH + "test_11_duplication.json")
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
            myfile.send_product(JSON_TEST_PATH + "test_12_deletion.json")
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
            myfile.send_product(JSON_TEST_PATH + "test_12_duplication.json")
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
            myfile.send_product(JSON_TEST_PATH + "test_13_modification.json")
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
            myfile.send_product(JSON_TEST_PATH + "test_11_deletion.json")
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
            myfile.send_product(JSON_TEST_PATH + "test_14_duplication.json")
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
            myfile.send_product(JSON_TEST_PATH + "test_15_deletion.json")
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
            myfile.send_product(JSON_TEST_PATH + "test_15_duplication.json")
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
            myfile.send_product(JSON_TEST_PATH + "test_16_deletion.json")
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
            myfile.send_product(JSON_TEST_PATH + "test_16_duplication.json")
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
            myfile.send_product(JSON_TEST_PATH + "test_17_deletion.json")
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
            myfile.send_product(JSON_TEST_PATH + "test_17_duplication.json")
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
            myfile.send_product(JSON_TEST_PATH + "test_18_deletion.json")
        self.assertEqual("Clave errónea", cm.exception.message)

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
            myfile.send_product(JSON_TEST_PATH + "test_18_duplication.json")
        self.assertEqual("Clave errónea", cm.exception.message)

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
            myfile.send_product(JSON_TEST_PATH + "test_19_deletion.json")
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
            myfile.send_product(JSON_TEST_PATH + "test_19_duplication.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_20_modification(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_20_modification.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_21_deletion(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_21_deletion.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_21_duplication(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_21_duplication.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_22_deletion(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_22_deletion.json")
        self.assertEqual("OrderID too short", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_22_duplication(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_22_duplication.json")
        self.assertEqual("OrderID too long", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_23_deletion(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_23_deletion.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_23_duplication(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_23_duplication.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_24_deletion(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_24_deletion.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_24_duplication(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_24_duplication.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_25_deletion(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_25_deletion.json")
        self.assertEqual("Clave errónea", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_25_duplication(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_25_duplication.json")
        self.assertEqual("Clave errónea", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_26_deletion(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_26_deletion.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_26_duplication(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_26_duplication.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_27_modification(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_27_modification.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_28_deletion(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_28_deletion.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_28_duplication(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_28_duplication.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_29_deletion(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_29_deletion.json")
        self.assertEqual("Email no valido", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_29_duplication(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_29_duplication.json")
        self.assertEqual("Email no valido", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_30_deletion(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_30_deletion.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_30_duplication(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_30_duplication.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_31_modification(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_31_modification.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_32_modification(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_32_modification.json")
        self.assertEqual("Clave errónea", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_33_modification(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_33_modification.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_34_modification(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_34_modification.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_35_modification(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_35_modification.json")
        self.assertEqual("OrderID no está en hexadecimal", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_36_modification(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_36_modification.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_37_modification(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_37_modification.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_38_modification(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_38_modification.json")
        self.assertEqual("Clave errónea", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_39_modification(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_39_modification.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_40_modification(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_40_modification.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_41_deletion(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_41_deletion.json")
        self.assertEqual("Email no valido", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_41_duplication(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_41_duplication.json")
        self.assertEqual("Email no valido", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_42_deletion(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_42_deletion.json")
        self.assertEqual("Email no valido", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_42_duplication(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_42_duplication.json")
        self.assertEqual("Email no valido", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_43_deletion(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_43_deletion.json")
        self.assertEqual("Email no valido", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_43_duplication(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_43_duplication.json")
        self.assertEqual("Email no valido", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_44_deletion(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_44_deletion.json")
        self.assertEqual("Email no valido", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_44_duplication(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_44_duplication.json")
        self.assertEqual("Email no valido", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_45_deletion(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_45_deletion.json")
        self.assertEqual("Email no valido", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_45_duplication(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_45_duplication.json")
        self.assertEqual("Email no valido", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_46_modification(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_46_modification.json")
        self.assertEqual("JSON Decode error - Wrong JSON format", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_47_modification(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_47_modification.json")
        self.assertEqual("Email no valido", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_48_modification(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_48_modification.json")
        self.assertEqual("Email no valido", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_49_modification(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_49_modification.json")
        self.assertEqual("Email no valido", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_50_modification(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_50_modification.json")
        self.assertEqual("Email no valido", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_51_modification(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_51_modification.json")
        self.assertEqual("Email no valido", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_orderid_31(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_orderID_31.json")
        self.assertEqual("OrderID too short", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

    def test_orderid_33(self):
        """
        test wrong
        """
        file_store = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        myfile = OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            myfile.send_product(JSON_TEST_PATH + "test_orderID_33.json")
        self.assertEqual("OrderID too long", cm.exception.message)

        if os.path.isfile(file_store):
            self.fail("Fallo: no debería haber file_store")

if __name__ == '__main__':
    unittest.main()
