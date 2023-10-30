import pytest
import unittest
from Config.config import login_data
from Sge_functions.sge_functions2 import sge_functions2
from steps import mostrador_simple_steps
#from ddt import ddt, file_data
from Config.config import images


#@ddt
class SgeUnittest(unittest.TestCase):

    #@file_data("./Config/TestDataset/dataSet_ddt_invoice_credit_simple_order.json")
    @pytest.mark.flaky(reruns=1)
    def test_inv_mostrador_simple(self):
        #print("Test using: "+supplier)

        sge_funct = sge_functions2()
        print("------------------------------Test to Create invoice Mostrador Simple Order")
        print("Trying to Connect...")
        sge_funct.sge_connection(login_data.linux_username, login_data.ip, login_data.password)
        print("Validating connection...")
        assert sge_funct.validate_adm_sge_connection(images.img_sge_adm_pantalla_inicial), "Error Found, SGE Connection Failed!!"
        mostrador_simple_steps.create_mostrador_simple_inv(sge_funct)
        print("Validating invoice creation")
        assert sge_funct.validating_invoice()


    def tearDown(self):
        sge_funct = sge_functions2()
        sge_funct.close_sge_session()


if __name__ == '__main__':
    unittest.main()

