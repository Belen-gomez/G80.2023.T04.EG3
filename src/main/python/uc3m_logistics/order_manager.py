"""Module """
from .order_request import OrderRequest
from .order_management_exception import OrderManagementException

class OrderManager:
    """Class for providing the methods for managing the orders"""
    def __init__(self):
        pass

    @staticmethod
    def validate_ean13(eAn13):
        """

        :param eAn13:
        :return:
        """
        #  La función validateEan13 en primer lugar comprueba si la longitud del código es distinta de 13, si es así.
        #  la función devuelve un False.
        if len(eAn13) < 13:
            raise OrderManagementException("Invalid EAN13 code len < 13")
        if len(eAn13) > 13:
            raise OrderManagementException("Invalid EAN13 code len > 13")
        #  El siguiente for comprueba el código de barras y si hay algun valor que no esté entre 0 y 9, este da error.
        for i in eAn13:
            if i not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                raise OrderManagementException("Invalid EAN13 code sum")
        suma = 0
        #  Este for hace la validación del código de barras, multiplicando las posiciones impares del código por 1 y
        #  las pares por 3. En nuestro caso, como el for empieza en 0, la primera posicion será par en lugar de impar
        #  por lo que se multiplicarán las impares por 3 y las pares por 1.
        for i in range(len(eAn13) - 1):
            digito = int(eAn13[i])
            if i % 2 == 0:
                suma += digito
            else:
                suma += digito * 3
        #  Finalmente a la suma se le añade la última posición del código y si esta suma es múltiplo de 10,
        #  la función devolverá True, ya que el código estaría validado. Si no es múltiplo de 10 devolverá False
        suma += int(eAn13[-1])
        if suma % 10 != 0:
            raise OrderManagementException("Invalid EAN13 code sum")
        return True


    def register_order (self, product_id, address, order_type, phone, zip_code):
        self.validate_ean13(eAn13=product_id)
        if order_type!= "PREMIUM" and order_type!= "REGULAR":
            raise OrderManagementException("Order type wrong")
        if len(address<20):
            raise OrderManagementException("Address too short")
        if len(address>20):
            raise OrderManagementException("Address too long")
        my_order = OrderRequest(product_id=product_id, delivery_address=address, order_type=order_type, phone_number=phone, zip_code=zip_code)

        return my_order.order_id