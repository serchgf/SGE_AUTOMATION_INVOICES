import logging
import unittest

import pytest
from _pytest import mark

from Config.config import login_data, txt_files_path
from Sge_functions.sge_functions2 import sge_functions2
from steps import MTC_INVSGE_024_steps as cmd_steps
#from ddt import ddt, file_data

from Config.config import images


#@ddt
class MTC_ASGE_024_Tests(unittest.TestCase):


    #@file_data("./Config/TestDataset/dataSet_ddt_invoice_credit_simple_order.json")
    @pytest.mark.flaky(reruns=1)
    def test_MTC_ASGE_024(self):
        #print("Test using: "+supplier)

        sge_funct = sge_functions2()
        logging.info("------------------------------Test to Create invoice Credit Massive Order")
        print("------------------------------Test to Create invoice Credit Massive Order")
        print("Trying to Connect...")
        sge_funct.sge_connection(login_data.linux_username, login_data.ip, login_data.password)
        print("Validating connection...")
        assert sge_funct.validate_adm_sge_connection(images.img_sge_adm_pantalla_inicial), "Error Found, SGE Connection Failed!!"
        cmd_steps.MTC_INVSGE_024_steps(sge_funct, txt_files_path.carga_masiva_50_txt)

        print("Validating invoice creation")
        assert sge_funct.validating_invoice_50(), "Error, Invoice not created"
        print("Invoice created succesfull")

    def tearDown(self):
        sge_funct = sge_functions2()
        #sge_funct.close_sge_session()


if __name__ == '__main__':
    unittest.main()

