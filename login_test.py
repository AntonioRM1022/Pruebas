import unittest
from unittest.mock import patch
from io import StringIO
from Punto_venta import Login

class TestLogin(unittest.TestCase):
    @patch('builtins.input', side_effect=['Tadeo', '1234'])
    def test_login_successful(self, mock_input):
        login = Login()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            login.usuario()
            self.assertEqual(fake_out.getvalue().strip(), "Inicio de sesión exitoso.")

    @patch('builtins.input', side_effect=['InvalidUser', 'InvalidPass'])
    def test_login_unsuccessful(self, mock_input):
        login = Login()
        with self.assertRaises(SystemExit):
            login.usuario()

if __name__ == '__main__':
    unittest.main()
