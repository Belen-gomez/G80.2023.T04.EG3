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
    def iniciar(self):
        """
        borra los almacenes
        """
        file_store = JSON_STORE_PATH + "store_request.json"
        if os.path.isfile(file_store):
            os.remove(file_store)
        file_delivery = JSON_STORE_PATH + "store_delivery.json"
        if os.path.isfile(file_delivery):
            os.remove(file_delivery)
        file_shipping = JSON_STORE_PATH + "store_shipping.json"
        if os.path.isfile(file_shipping):
            os.remove(file_shipping)
        return True

    def test_ok(self):
        """
        test ok
        """
        self.iniciar()
        my_freezer = freeze_time("2023-02-19")
        my_freezer.start()

        my_order = OrderManager()
        my_order.register_order(product_id="8421691423220", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28005", phone="123456789", order_type="REGULAR")

        file_test = JSON_TEST_PATH + "test_ok.json"
        my_order.send_product(file_test)
        my_freezer.stop()

        my_freezer = freeze_time("2023-02-26")
        my_freezer.start()
        my_value = my_order.deliver_product("82fcbe31129725fd78bbde4945ec65eb1560a0f593d114e0b1e52943bc33f549")
        self.assertEqual(my_value, True)

        file_store = JSON_STORE_PATH + "store_delivery.json"

        with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item["Tracking_code"] == "82fcbe31129725fd78bbde4945ec65eb1560a0f593d114e0b1e52943bc33f549":
                found = True
        my_freezer.stop()
        self.assertTrue(found)


    def test_ok_ya_almacenado(self):
        """
        test ok
        """
        self.iniciar()
        my_freezer = freeze_time("2023-02-19")
        my_freezer.start()

        my_order = OrderManager()
        my_order.register_order(product_id="8421691423220", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28005", phone="123456789", order_type="REGULAR")

        file_test = JSON_TEST_PATH + "test_ok.json"
        my_order.send_product(file_test)
        my_freezer.stop()

        my_freezer = freeze_time("2023-02-26")
        my_freezer.start()

        my_order.deliver_product("82fcbe31129725fd78bbde4945ec65eb1560a0f593d114e0b1e52943bc33f549")
        my_order.deliver_product("82fcbe31129725fd78bbde4945ec65eb1560a0f593d114e0b1e52943bc33f549")

        file_store = JSON_STORE_PATH + "store_delivery.json"

        with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
            data_list = json.load(file)
        my_freezer.stop()
        self.assertEqual(1, len(data_list))

    def test_tracking_num_65(self):
        """
        test wrong
        """
        self.iniciar()
        my_freezer = freeze_time("2023-02-19")
        my_freezer.start()

        my_order = OrderManager()
        my_order.register_order(product_id="8421691423220", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28005", phone="123456789", order_type="REGULAR")

        file_test = JSON_TEST_PATH + "test_ok.json"
        my_order.send_product(file_test)
        my_freezer.stop()

        my_freezer = freeze_time("2023-02-26")
        my_freezer.start()

        with self.assertRaises(OrderManagementException) as cm:
            my_order.deliver_product("82fcbe31129725fd78bbde4945ec65eb1560a0f593d114e0b1e52943bc33f549a")
        self.assertEqual("Tracking number too long", cm.exception.message)
        my_freezer.stop()
        file_delivery = JSON_STORE_PATH + "store_delivery.json"
        if os.path.isfile(file_delivery):
            self.fail("Fallo: no debería haber file_store")

    def test_tracking_num_63(self):
        """
        test wrong
        """
        self.iniciar()
        my_freezer = freeze_time("2023-02-19")
        my_freezer.start()

        my_order = OrderManager()
        my_order.register_order(product_id="8421691423220", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28005", phone="123456789", order_type="REGULAR")

        file_test = JSON_TEST_PATH + "test_ok.json"
        my_order.send_product(file_test)
        my_freezer.stop()
        my_freezer = freeze_time("2023-02-26")
        my_freezer.start()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.deliver_product("82fcbe31129725fd78bbde4945ec65eb1560a0f593d114e0b1e52943bc33f54")
        self.assertEqual("Tracking number too short", cm.exception.message)
        my_freezer.stop()
        file_delivery = JSON_STORE_PATH + "store_delivery.json"
        if os.path.isfile(file_delivery):
            self.fail("Fallo: no debería haber file_store")

    def test_tracking_num_0(self):
        """
        test wrong
        """
        self.iniciar()
        my_freezer = freeze_time("2023-02-19")
        my_freezer.start()

        my_order = OrderManager()
        my_order.register_order(product_id="8421691423220", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28005", phone="123456789", order_type="REGULAR")

        file_test = JSON_TEST_PATH + "test_ok.json"
        my_order.send_product(file_test)
        my_freezer.stop()

        my_freezer = freeze_time("2023-02-26")
        my_freezer.start()

        with self.assertRaises(OrderManagementException) as cm:
            my_order.deliver_product("")
        self.assertEqual("Tracking number too short", cm.exception.message)
        my_freezer.stop()
        file_delivery = JSON_STORE_PATH + "store_delivery.json"
        if os.path.isfile(file_delivery):
            self.fail("Fallo: no debería haber file_store")

    def test_tracking_num_1(self):
        """
        test wrong
        """
        self.iniciar()
        my_freezer = freeze_time("2023-02-19")
        my_freezer.start()

        my_order = OrderManager()
        my_order.register_order(product_id="8421691423220", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28005", phone="123456789", order_type="REGULAR")

        file_test = JSON_TEST_PATH + "test_ok.json"
        my_order.send_product(file_test)
        my_freezer.stop()

        my_freezer = freeze_time("2023-02-26")
        my_freezer.start()

        with self.assertRaises(OrderManagementException) as cm:
            my_order.deliver_product("c")
        self.assertEqual("Tracking number too short", cm.exception.message)
        my_freezer.stop()
        file_delivery = JSON_STORE_PATH + "store_delivery.json"
        if os.path.isfile(file_delivery):
            self.fail("Fallo: no debería haber file_store")

    def test_tracking_num_2(self):
        """
        test wrong
        """
        self.iniciar()
        my_freezer = freeze_time("2023-02-19")
        my_freezer.start()

        my_order = OrderManager()
        my_order.register_order(product_id="8421691423220", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28005", phone="123456789", order_type="REGULAR")

        file_test = JSON_TEST_PATH + "test_ok.json"
        my_order.send_product(file_test)
        my_freezer.stop()

        my_freezer = freeze_time("2023-02-26")
        my_freezer.start()

        with self.assertRaises(OrderManagementException) as cm:
            my_order.deliver_product("c1")
        self.assertEqual("Tracking number too short", cm.exception.message)
        my_freezer.stop()
        file_delivery = JSON_STORE_PATH + "store_delivery.json"
        if os.path.isfile(file_delivery):
            self.fail("Fallo: no debería haber file_store")

    def test_tracking_num_not_hex(self):
        """
        test wrong
        """
        self.iniciar()
        my_freezer = freeze_time("2023-02-19")
        my_freezer.start()

        my_order = OrderManager()
        my_order.register_order(product_id="8421691423220", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28005", phone="123456789", order_type="REGULAR")

        file_test = JSON_TEST_PATH + "test_ok.json"
        my_order.send_product(file_test)
        my_freezer.stop()
        my_freezer = freeze_time("2023-02-26")
        my_freezer.start()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.deliver_product("c80509cf07K1efefcaba7ec55512f218a047925162f121fcac3fc008bfad810a")
        self.assertEqual("Tracking number no está en hexadecimal", cm.exception.message)
        my_freezer.stop()
        file_delivery = JSON_STORE_PATH + "store_delivery.json"
        if os.path.isfile(file_delivery):
            self.fail("Fallo: no debería haber file_store")

    def test_store_shipping_not_found(self):
        """
        test wrong
        """
        self.iniciar()
        my_order = OrderManager()
        my_order.register_order(product_id="8421691423220", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28005", phone="123456789", order_type="REGULAR")

        with self.assertRaises(OrderManagementException) as cm:
            my_order.deliver_product("9626d1c11d0f544588ab0b5be51279b32e96c9d35b956b782d9d8f4b813ec866")
        self.assertEqual("Store shipping not found", cm.exception.message)
        file_delivery = JSON_STORE_PATH + "store_delivery.json"
        if os.path.isfile(file_delivery):
            self.fail("Fallo: no debería haber file_store")

    def test_pedido_not_found(self):
        """
        test wrong
        """
        self.iniciar()
        my_freezer = freeze_time("2023-02-19")
        my_freezer.start()

        my_order = OrderManager()
        my_order.register_order(product_id="8421691423220", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28005", phone="123456789", order_type="REGULAR")

        file_test = JSON_TEST_PATH + "test_ok.json"
        my_order.send_product(file_test)
        my_freezer.stop()
        my_freezer = freeze_time("2023-02-26")
        my_freezer.start()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.deliver_product("9626d1c11d0f544588ab0b5be51279b32e96c9d35b956b782d9d8f4b813ec866")
        self.assertEqual("Pedido no encontrado", cm.exception.message)
        my_freezer.stop()
        file_delivery = JSON_STORE_PATH + "store_delivery.json"
        if os.path.isfile(file_delivery):
            self.fail("Fallo: no debería haber file_store")

    def test_fecha_not_valid(self):
        """
        test wrong
        """
        self.iniciar()
        my_freezer = freeze_time("2023-02-19")
        my_freezer.start()

        my_order = OrderManager()
        my_order.register_order(product_id="8421691423220", address="C/LISBOA,4, MADRID, SPAIN",
                                           zip_code="28005", phone="123456789", order_type="REGULAR")

        file_test = JSON_TEST_PATH + "test_ok.json"
        my_order.send_product(file_test)
        with self.assertRaises(OrderManagementException) as cm:
            my_order.deliver_product("82fcbe31129725fd78bbde4945ec65eb1560a0f593d114e0b1e52943bc33f549")
        self.assertEqual("Fecha incorrecta", cm.exception.message)
        my_freezer.stop()
        file_delivery = JSON_STORE_PATH + "store_delivery.json"
        if os.path.isfile(file_delivery):
            self.fail("Fallo: no debería haber file_store")

if __name__ == '__main__':
    unittest.main()
