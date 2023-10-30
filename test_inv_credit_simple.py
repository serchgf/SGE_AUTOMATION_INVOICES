import pytest
import unittest
from Config.config import login_data
from Sge_functions.sge_functions2 import sge_functions2
#from ddt import ddt, file_data
from Config.config import images
from steps import credito_simple_steps


#@ddt
class SgeUnittest(unittest.TestCase):

        #@file_data("./Config/TestDataset/dataSet_ddt_invoice_credit_simple_order.json")
    @pytest.mark.flaky(reruns=1)
    def test_create_invoice_credit_simple_order(self):

        # print("Test using: "+supplier)
        sge_funct = sge_functions2()
        print("------------------------------Test to Create invoice")
        sge_funct.sge_connection(login_data.linux_username, login_data.ip, login_data.password)
        print("Trying to Connect...")
        print("Validating connection...")
        assert sge_funct.validate_adm_sge_connection(images.img_sge_adm_pantalla_inicial), "Error de conexion"
        credito_simple_steps.crear_credito_simple_invoice(sge_funct)
        assert sge_funct.validating_invoice(), "Error en la validacion de la facturacion"
        print("Validacion realizada con exito")

    def tearDown(self):
        sge_funct = sge_functions2()
        sge_funct.close_sge_session()


if __name__ == '__main__':
    unittest.main()