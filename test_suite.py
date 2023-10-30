import unittest

from test_inv_mostrador_simple import SgeUnittest as mostrador_simple
from test_inv_credit_massive_order import SgeUnittest as orden_masiva
from test_inv_credit_simple import SgeUnittest as credito_simple


def suite():
    suite = unittest.TestSuite()
    suite.addTest(mostrador_simple('test_inv_mostrador_simple'))
    suite.addTest(orden_masiva('test_inv_credit_massive_order'))
    suite.addTest(credito_simple('test_create_invoice_credit_simple_order'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())