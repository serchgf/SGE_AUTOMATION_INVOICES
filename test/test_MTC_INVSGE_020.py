import logging
import unittest
import pytest
from Config.config import login_data, txt_files_path
from Sge_functions.sge_functions2 import sge_functions2
from steps import MTC_INVSGE_020_steps as inv_steps
# from ddt import ddt, file_data
from Config.config import images


# @ddt
class MTC_AINVSGE_020_Tests(unittest.TestCase):

    # @file_data("./Config/TestDataset/dataSet_ddt_invoice_credit_simple_order.json")
    #@pytest.mark.flaky(reruns=1)
    def test_MTC_AINVSGE_020(self):
        # print("Test using: "+supplier)

        sge_funct = sge_functions2()
        logging.info("------------------------------Test to Create Facturacion sencilla contado foraneo kit")
        print("------------------------------Test to Create Facturacion sencilla contado foraneo kit")
        print("Trying to Connect...")
        sge_funct.sge_connection(login_data.linux_username, login_data.ip, login_data.password)
        print("Validating connection...")
        assert sge_funct.validate_adm_sge_connection(images.img_sge_adm_pantalla_inicial), "Error Found, SGE Connection Failed!!"
        inv_steps.MTC_INVSGE_020_steps(sge_funct)
        print("Validating invoice creation")
        assert sge_funct.validating_invoice(), "Error, Invoice not created"
        print("Invoice created succesfull")

    def tearDown(self):
        sge_funct = sge_functions2()
        #sge_funct.close_sge_session()


if __name__ == '__main__':
    unittest.main()

