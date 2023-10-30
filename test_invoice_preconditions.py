import unittest

import pytest

from Config.config import login_data, images
from Sge_functions.sge_functions2 import sge_functions2
from preconditions import change_hour_rfc_steps


#@ddt
class SgeUnittest(unittest.TestCase):

        #@file_data("./Config/TestDataset/dataSet_ddt_invoice_credit_simple_order.json")
    @pytest.mark.flaky(reruns=1)
    def test_preconditions_rfc_change_date(self):
        sge_funct = sge_functions2()
        print("------------------------------Test to Create invoice")
        sge_funct.sge_connection(login_data.linux_username, login_data.ip, login_data.password)
        print("Trying to Connect...")
        print("Validating connection...")
        assert sge_funct.validate_adm_sge_connection(images.img_sge_adm_pantalla_inicial), "Error de conexion"
        change_hour_rfc_steps.pre_change_rfc_date(sge_funct)

if __name__ == '__main__':
    unittest.main()