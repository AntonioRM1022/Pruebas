import unittest
from unittest.mock import patch
from io import StringIO
from Punto_venta import VentaDiscos

class TestVentaDiscos(unittest.TestCase):
    @patch('builtins.input', side_effect=[2, 300, 1, 300])
    def test_venta_discos_successful(self, mock_input):
        venta_discos = VentaDiscos()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            venta_discos.discos()
            expected_output = "Vendedor: Tadeo\nProducto: Discos\nCantidad: 2\nTotal: $300\nPago: $300\nCambio: $0"
            self.assertIn(expected_output, fake_out.getvalue())

if __name__ == '__main__':
    unittest.main()
