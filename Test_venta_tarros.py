import unittest
from unittest.mock import patch
from io import StringIO
from Punto_venta import VentaTarros

class TestVentaTarros(unittest.TestCase):
    @patch('builtins.input', side_effect=[3, 400, 1, 400])
    def test_venta_tarros_successful(self, mock_input):
        venta_tarros = VentaTarros()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            venta_tarros.tarros()
            self.assertIn("Pago exitoso", fake_out.getvalue())


if __name__ == '__main__':
    unittest.main()
