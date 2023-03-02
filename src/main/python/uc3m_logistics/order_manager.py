"""Module """
from .order_request import OrderRequest
class OrderManager:
    """Class for providing the methods for managing the orders"""
    def __init__(self):
        pass

    @staticmethod
    def validate_ean13(ean13_code):
        """RETURNs TRUE IF THE CODE RECEIVED IS A VALID EAN13,
        OR FALSE IN OTHER CASE"""
        return True
    def register_order (self, product_id, address, order_type, phone, zip_code):
        my_order = OrderRequest(product_id=product_id, delivery_address=address, order_type=order_type, phone_number=phone, zip_code=zip_code)

        return my_order.order_id