"""Module """
import json
import re
from pathlib import Path
from .order_request import OrderRequest
from .order_shipping import OrderShipping
from .order_management_exception import OrderManagementException

JSON_FILE_PATH = str(Path.home()) + "/PycharmProjects/G80.2023.T04.EG3/src/Json/store/"
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
                raise OrderManagementException("Invalid EAN13 code string")
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

    def register_order(self, product_id, address, order_type, phone, zip_code):
        """
        :param product_id:
        :param address:
        :param order_type:
        :param phone:
        :param zip_code:
        :return: order_id
        """
        #  comprobamos que el eAn13 es del formato correcto
        self.validate_ean13(eAn13=product_id)
        #  comprobamos que el order_type es correcto. En caso contrario se devuelve una excepción
        if order_type not in ("REGULAR", "PREMIUM"):
            raise OrderManagementException("Order type wrong")
        #  comprobamos que la dirección es correcta. En caso contrario se devuelve una excepción
        #  para ello comprobamos la longitud y el formato
        if len(address) < 20:
            raise OrderManagementException("Address too short")
        if len(address) > 100:
            raise OrderManagementException("Address too long")
        espacio = False
        i = 0
        while i < len(address) and not espacio:
            if address[i] == ' ' and i+1!= len(address):
                espacio = True
            i+=1
        if not espacio:
            raise OrderManagementException("Direccion sin espacios")

        #  comprobamos que el teléfono es correcto. En caso contrario se devuelve una excepción
        #  para ello comprobamos la longitud y el formato
        for i in phone:
            if i not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                raise OrderManagementException("Phone number is a string")
        if len(phone) < 9:
            raise OrderManagementException("Phone number too short")
        if len(phone) > 9:
            raise OrderManagementException("Phone number too long")

        #  comprobamos que el teléfono es correcto. En caso contrario se devuelve una excepción
        #  para ello comprobamos la longitud y el formato
        for i in zip_code:
            if i not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                raise OrderManagementException("Zip code is a string")
        j = 0
        if int(zip_code[j]) > 5:
            raise OrderManagementException("Zip code is not valid")
        if int(zip_code[j]) == 5 and int(zip_code[j+1] > 2):
            raise OrderManagementException("Zip code is not valid")
        if len(zip_code) < 5:
            raise OrderManagementException("Zip code too short")
        if len(zip_code) > 5:
            raise OrderManagementException("Zip code too long")

        #  creamos el objeto de la clase OrderRequest
        my_order = OrderRequest(product_id=product_id, delivery_address=address, order_type=order_type,
                                phone_number=phone, zip_code=zip_code)

        #  abrimos el fichero del almacén y guardamos los dato en una lista (data_list)
        #  en caso de que el fichero esté vacío data_list se crea vacía
        file_store = JSON_FILE_PATH + "store_request.json"
        try:
            with open(file_store, "r", encoding="utf8", newline="") as file:
                data_list = json.load(file)
        except FileNotFoundError:
            data_list = []
        except json.JSONDecodeError as ex:
            raise OrderManagementException("JSON Decode error - Wrong JSON format") from ex

        #  comprobamos que el pedido no se encuentra ya en el almacén
        found = False
        for item in data_list:
            if item["_OrderRequest__order_id"] == my_order.order_id:
                found = True
        #  si el pedido no se había almacenado antes, se añade a la lista de pedidos en forma de diccionario y se añade al almacén
        if not found:
            data_list.append(my_order.__dict__)
            try:
                with open(file_store, "w", encoding="utf8", newline="") as file:
                    json.dump(data_list, file, indent=2)
            except FileNotFoundError as ex:
                raise OrderManagementException("Wrong file or file path") from ex

        #  la función devuelve el order_id del nuevo pedido
        return my_order.order_id

    def send_product(self, input_file):
        """
        :param input_file:
        :return: tracking code
        """
        #  abrimos el fichero input_file en modo lectura.
        #  guardamos los datos en data_list
        #  si el fichero no se encuentra o no tiene formato JSON la función devuelve una excepción
        try:
            with open(input_file, "r", encoding = "utf8", newline="") as file:
                data_list = json.load(file)
        except FileNotFoundError as exc:
            raise OrderManagementException("Archivo no encontrado") from exc
        except json.JSONDecodeError as ex:
            raise OrderManagementException("JSON Decode error - Wrong JSON format") from ex

        #  si el archivo está vacío devuelve una excepción
        if data_list[0] == {}:
            raise OrderManagementException("Pedido vacío")

        #  si la clave es errónea devuelve una excepción
        keys = data_list[0].keys()
        for item in keys:
            if item not in ("OrderID", "ContactEmail"):
                raise OrderManagementException("Clave errónea")

        #  comprobamos que el OrderID es una valor hexadecimal de 32 dígitos
        orderid = data_list[0]["OrderID"]
        for i in orderid:
            if i not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]:
                raise OrderManagementException("OrderID no está en hexadecimal")
        if len(orderid) < 32:
            raise OrderManagementException("OrderID too short")
        if len(orderid) > 32:
            raise OrderManagementException("OrderID too long")

        #  comprobamos que el email sigue el patrón correcto. En caso contrario devuelve una excepción
        email_pattern = re.compile(r'^[A-Za-z0-9]+@[A-Za-z0-9]+\.[a-z]{2,3}$')
        my_email = data_list[0]["ContactEmail"]
        valido = email_pattern.match(my_email)
        if not valido:
            raise OrderManagementException("Email no valido")

        #  abrimos el fichero store_request, donde están almacenados los pedidos de la función register_order
        #  guardamos los datos en store
        #  si el fichero no se encuentra o no tiene formato JSON la función devuelve una excepción
        file_store = JSON_FILE_PATH + "store_request.json"
        try:
            with open(file_store, "r", encoding="utf8", newline="") as file_2:
                store = json.load(file_2)
        except FileNotFoundError as exc:
            raise OrderManagementException("Almacén no encontrado") from exc
        except json.JSONDecodeError as ex:
            raise OrderManagementException("JSON Decode error - Wrong JSON format") from ex

        #  comprobamos que el pedido está en el almacén. En caso contrario devuelve una excepción
        encontrado = False
        pedido_almacen = None
        for item in store:
            if item["_OrderRequest__order_id"] == orderid:
                encontrado = True
                pedido_almacen = item
        if not encontrado:
            raise OrderManagementException("El pedido no se encontró entre los pedidos registrados")
        #  se crea un objeto de la clase OrderShipping con los atributos del pedido.
        #  Order_id y delivery_email son datos del fichero de entrada input_file
        #  El resto de datos los obtenemos de store_request
        pedido = OrderShipping(product_id=pedido_almacen["_OrderRequest__product_id"], order_id=orderid, delivery_email=my_email, order_type=pedido_almacen["_OrderRequest__order_type"])

        #  abrimos el almacén y guardamos sus datos en almacen_pedidos
        #  si no existe el fichero, la lista almacen_pedidos se crea vacía
        shipping_store = JSON_FILE_PATH + "store_shipping.json"
        try:
            with open(shipping_store, "r", encoding="utf8", newline="") as file_3:
                almacen_pedidos = json.load(file_3)
        except FileNotFoundError as ex:
            almacen_pedidos = []
        except json.JSONDecodeError as ex:
            raise OrderManagementException("JSON Decode error - Wrong JSON format") from ex

        #  comprobamos que el pedido no esté ya en el almacén
        #  si ya está en el almacén no se vuelve a meter
        encontra2 = False
        for item in almacen_pedidos:
            if item["_OrderShipping__order_id"] == pedido.order_id:
                encontra2 = True

        #  metemos el nuevo pedido en el almacén
        if not encontra2:
            almacen_pedidos.append(pedido.__dict__)
            try:
                with open(shipping_store, "w", encoding="utf8", newline="") as file:
                    json.dump(almacen_pedidos, file, indent=2)
            except FileNotFoundError as ex:
                raise OrderManagementException("Wrong file or file path") from ex

        return pedido.tracking_code

    def deliver_product(self, tracking_number):
        """

        :param tracking_number:
        :return: True
        """

        if len(tracking_number) > 64:
            raise OrderManagementException("Tracking number too long")

        if len(tracking_number) < 64:
            raise OrderManagementException("Tracking number too short")

        for i in tracking_number:
            if i not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]:
                raise OrderManagementException("Tracking numberno está en hexadecimal")

        shipping_store = JSON_FILE_PATH + "store_shipping.json"
        try:
            with open(shipping_store, "r", encoding="utf8", newline="") as file_3:
                almacen_pedidos = json.load(file_3)
        except FileNotFoundError as ex:
            raise OrderManagementException("Store shipping not found") from ex
        except json.JSONDecodeError as ex:
            raise OrderManagementException("JSON Decode error - Wrong JSON format") from ex

        encontra2 = False
        delivery_date = None
        for item in almacen_pedidos:
            if item["_OrderShipping__tracking_code"] == tracking_number:
                encontra2 = True
                delivery_date = item["_OrderShipping__delivery_day"]
        if not encontra2:
            raise OrderManagementException("Pedido no encontrado")

        diccionario= \
            {
            "Tracking_code":tracking_number,
            "Delivery_date":delivery_date

        }

        delivery_store = JSON_FILE_PATH + "store_delivery.json"
        try:
            with open(delivery_store, "r", encoding="utf8", newline="") as file_4:
                data = json.load(file_4)
        except FileNotFoundError as ex:
            data = []
        except json.JSONDecodeError as ex:
            raise OrderManagementException("JSON Decode error - Wrong JSON format") from ex

        found = False
        for item in data:
            if item["Tracking_code"] == tracking_number:
                found = True
        if not found:
            data.append(diccionario)
            try:
                with open(delivery_store, "w", encoding="utf8", newline="") as file:
                    json.dump(data, file, indent=2)
            except FileNotFoundError as ex:
                raise OrderManagementException("Wrong file or file path") from ex

        return True
