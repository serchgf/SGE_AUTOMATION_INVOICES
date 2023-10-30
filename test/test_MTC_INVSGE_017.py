import logging
import unittest
import pytest
from Config.config import login_data, txt_files_path
from Sge_functions.sge_functions2 import sge_functions2
from steps import MTC_INVSGE_017_steps as inv_steps
# from ddt import ddt, file_data
from Config.config import images
from pytest import mark

# @ddt
class MTC_INVSGE_017_Tests(unittest.TestCase):

    # @file_data("./Config/TestDataset/dataSet_ddt_invoice_credit_simple_order.json")
    #@pytest.mark.flaky(reruns=1)
    #@mark.demo
    def test_MTC_INVSGE_017(self):
        # print("Test using: "+supplier)

        sge_funct = sge_functions2()
        logging.info("------------------------------Test to Create Facturacion sencilla credito foraneo kit")
        print("------------------------------Test to Create Facturacion sencilla credito foraneo kit")
        print("Trying to Connect...")
        sge_funct.sge_connection(login_data.linux_username, login_data.ip, login_data.password)
        print("Validating connection...")
        assert sge_funct.validate_adm_sge_connection(images.img_sge_adm_pantalla_inicial), "Error Found, SGE Connection Failed!!"
        inv_steps.MTC_INVSGE_017_steps(sge_funct)
        print("Validating invoice creation")
        assert sge_funct.validating_invoice(), "Error, Invoice not created"
        print("Invoice created succesfull")

    def tearDown(self):
        sge_funct = sge_functions2()
        sge_funct.close_sge_session()


if __name__ == '__main__':
    unittest.main()

