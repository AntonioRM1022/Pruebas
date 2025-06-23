import unittest
from unittest.mock import patch
from io import StringIO
from Punto_venta import VentaDiscos, VentaTarros, VentaTazas

class TestIntegrated(unittest.TestCase):
    @patch('builtins.input', side_effect=[5, 800, 800, 2])
    def test_venta_discos_sinticket(self, mock_input):
        venta_discos = VentaDiscos()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            venta_discos.discos()
            self.assertIn("Pago exitoso", fake_out.getvalue())

    @patch('builtins.input', side_effect=[3, 800, 800, 2])
    def test_venta_tarros_sinticketl(self, mock_input):
        venta_tarros = VentaTarros()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            venta_tarros.tarros()
            self.assertIn("Pago exitoso", fake_out.getvalue())

    @patch('builtins.input', side_effect=[2, 800, 800, 2])
    def test_venta_tazas_sinticket(self, mock_input):
        venta_tazas = VentaTazas()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            venta_tazas.tazas()
            self.assertIn("Pago exitoso", fake_out.getvalue())

if __name__ == '__main__':
    unittest.main()
