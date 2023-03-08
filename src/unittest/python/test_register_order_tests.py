"""class for testing the regsiter_order method"""
import unittest
from freezegun import freeze_time
from uc3m_logistics import OrderManager
from uc3m_logistics import OrderManagementException

class MyTestCase(unittest.TestCase):
    """class for testing the register_order method"""

    @freeze_time("2023-02-19")
    def test_register_order( self ):
        my_order = OrderManager()
        my_value = my_order.register_order(product_id= "8421691423220", address= "C/LISBOA,4, MADRID, SPAIN", zip_code= "28005", phone="+34123456789", order_type="REGULAR")
        self.assertEqual(my_value, "6f651f23a6af8d79e5a30276d136b1ee")

    def test_with_product_code_wrong(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            value = my_order.register_order("842169142322A", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN", "+34123456789", "28005")
            #valor =my_order.validate_ean13("842169142322A")
            self.assertEqual("Invalid EAN13 code string", cm.exception.message)

    def test_with_product_code_wrong2(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            value = my_order.register_order("8421691423225", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN", "+34123456789", "28005")
            #valor =my_order.validate_ean13("842169142322A")
            self.assertEqual("Invalid EAN13 code sum", cm.exception.message)

if __name__ == '__main__':
    unittest.main()
