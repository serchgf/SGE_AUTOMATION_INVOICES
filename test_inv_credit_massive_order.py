import logging
import unittest

import pytest
from _pytest import mark

from Config.config import login_data, txt_files_path
from Sge_functions.sge_functions2 import sge_functions2
from steps import credit_massive_order_steps as cmo_steps
#from ddt import ddt, file_data

from Config.config import images


#@ddt
class SgeUnittest(unittest.TestCase):


    #@file_data("./Config/TestDataset/dataSet_ddt_invoice_credit_simple_order.json")
    @pytest.mark.flaky(reruns=1)
    def test_inv_credit_massive_order(self):
        #print("Test using: "+supplier)

        sge_funct = sge_functions2()
        logging.info("------------------------------Test to Create invoice Credit Massive Order")
        print("------------------------------Test to Create invoice Credit Massive Order")
        print("Trying to Connect...")
        sge_funct.sge_connection(login_data.linux_username, login_data.ip, login_data.password)
        print("Validating connection...")
        assert sge_funct.validate_adm_sge_connection(images.img_sge_adm_pantalla_inicial), "Error Found, SGE Connection Failed!!"
        cmo_steps.create_credit_massive_order_inv(sge_funct, txt_files_path.carga_masiva_txt)

        print("Validating invoice creation")
        assert sge_funct.validating_invoice(), "Error, Invoice not created"
        print("Invoice created succesfull")

    def tearDown(self):
        sge_funct = sge_functions2()
        sge_funct.close_sge_session()


if __name__ == '__main__':
    unittest.main()

