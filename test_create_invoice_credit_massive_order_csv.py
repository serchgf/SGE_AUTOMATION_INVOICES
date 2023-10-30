import unittest
from Config.config import login_data
from Config.config import csv_files_path
from Sge_functions.invoice_functions import SgeFunctions
#from ddt import ddt, file_data
from Config.invoice_credit_massive_order_cmds import invoice_commands
from Config.config import images
import pyautogui as pa


#@ddt
class SgeUnittest(unittest.TestCase):

    #@file_data("./Config/TestDataset/dataSet_ddt_invoice_credit_simple_order.json")
    def test_create_invoice_credit_massive_order(self):
        #print("Test using: "+supplier)
        sge_funct = SgeFunctions()
        print("------------------------------Test to Create invoice Credit Massive Order")
        sge_funct.connection(login_data.linux_username, login_data.ip, login_data.password)
        print("Trying to Connect...")
        print("Validating connection...")
        flag = sge_funct.validate_connection()
        print(flag)
        if flag:
            # sge_funct.create_credit_invoice_simple_order()
            lista_objetos = sge_funct.crear_lista_objetos(csv_files_path.csv_invoice_credit_massive_order)
            sge_funct.create_general_invoice(lista_objetos, images.img_rclick_carga_masiva, None)
            print("Validating invoice creation")
            sge_funct.validating_invoice()
        else:
            print("Error Found, Connection Failed!!")
            assert flag

    def tearDown(self):
        sge_funct = SgeFunctions()
        sge_funct.close_invoice_session()


if __name__ == '__main__':
    unittest.main()

