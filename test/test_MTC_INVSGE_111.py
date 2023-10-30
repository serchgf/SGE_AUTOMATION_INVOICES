import pytest
import unittest
from Config.config import login_data, files
from Sge_functions.sge_functions2 import sge_functions2
#from ddt import ddt, file_data
from Config.config import images
from steps import MTC_INVSGE_011_steps
import json

def leer_datos_desde_json(json_path):
    with open(json_path) as archivo:
        datos = json.load(archivo)
    return datos.values()


def cargar_datos_prueba(json_path):
    datos = leer_datos_desde_json(json_path)
    return datos



#@ddt
class MTC_ASGE_111_Tests:

        #@file_data("./Config/TestDataset/dataSet_ddt_invoice_credit_simple_order.json")
    @pytest.mark.flaky(reruns=1)

    @pytest.mark.parametrize("data", cargar_datos_prueba(files.change_rfc_date))
    def test_MTC_INVSGE_111(self, data):
        print(data["rfc"])
        # print("Test using: "+supplier)
        sge_funct = sge_functions2()
        print("------------------------------Test to Create invoice")
        sge_funct.sge_connection(login_data.linux_username, login_data.ip, login_data.password)
        print("Trying to Connect...")
        print("Validating connection...")
        assert sge_funct.validate_adm_sge_connection(images.img_sge_adm_pantalla_inicial), "Error de conexion"
        MTC_INVSGE_011_steps.MTC_INVSGE_011_steps(sge_funct, data)
        # assert sge_funct.validating_invoice(), "Error en la validacion de la facturacion"
        # print("Validacion realizada con exito")

    def tearDown(self):
        sge_funct = sge_functions2()
        sge_funct.close_sge_session()


if __name__ == '__main__':
    unittest.main()