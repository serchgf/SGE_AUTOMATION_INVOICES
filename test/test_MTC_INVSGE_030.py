import logging
import unittest
import pytest
from Config.config import login_data, txt_files_path
from Sge_functions.sge_functions2 import sge_functions2
from steps import MTC_INVSGE_030_steps as inv_steps
# from ddt import ddt, file_data
from Config.config import images


# @ddt
class MTC_AINVSGE_030_Tests(unittest.TestCase):

    # @file_data("./Config/TestDataset/dataSet_ddt_invoice_credit_simple_order.json")
    #@pytest.mark.flaky(reruns=1)
    def test_MTC_AINVSGE_030(self):
        # print("Test using: "+supplier)

        sge_funct = sge_functions2()
        logging.info("------------------------------Test to Create Cancelacion factura credito Facturacion")
        print("------------------------------Test to Create Cancelacion factura credito Facturacion")
        print("Trying to Connect...")
        sge_funct.sge_connection(login_data.linux_username, login_data.ip, login_data.password)
        print("Validating connection...")
        assert sge_funct.validate_adm_sge_connection(images.img_sge_adm_pantalla_inicial), "Error Found, SGE Connection Failed!!"
        inv_steps.MTC_INVSGE_030_steps(sge_funct, images.img_inicio_factura)
        print("Validating invoice creation")
        assert sge_funct.validate_image_x(images.img_validacion_devolucion_total), "Error, Invoice Cancellation not created"
        print("Invoice Cancellation created succesfull")

    def tearDown(self):
        sge_funct = sge_functions2()
        #sge_funct.close_sge_session()


if __name__ == '__main__':
    unittest.main()

