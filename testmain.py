import unittest
from unittest.mock import patch
from main import main

@patch("pprint.pprint")
@patch("builtins.input")

class Test4InLine(unittest.TestCase):

    def test_1_wins(self, patched_input, patched_print, *args):
        patched_input.side_effect = ["x", "y", "1", "2", "1", "2", "1", "2", "1", "n"]
        main()
        last_call = patched_print.call_count
        self.assertEqual(patched_print.call_args_list[last_call - 1][0][0],
                         "El juego ha terminado. Felicitaciones: Jugador 1, has ganado")

    def test_valuerror(self, patched_input, patched_print, *args):
        patched_input.side_effect = ["x", "y", "a", "q"]
        main()
        self.assertEqual(patched_print.call_args_list[1][0][0],
                         'No se ha ingresado un numero, intente nuevamente')
        patched_input.return_value = "q"

    def test_no_valid_number(self, patched_input, patched_print, *args):
        patched_input.side_effect = ["x", "y", "9", "q"]
        main()
        self.assertEqual(patched_print.call_args_list[1][0][0], 'La columna ingresada no existe, intente nuevamente')

    def test_full_no_space(self, patched_input, patched_print, *args):
        patched_input.side_effect = ["x", "y", "1", "1", "1", "1", "1", "1", "1", "1", "1", "q"]
        main()
        self.assertEqual(patched_print.call_args_list[9][0][0], 'La columna esta llena, elija otra')

    def test_column(self, patched_input, patched_print, *args):
        patched_input.side_effect = ["x", "y", "1", "2", "1", "2", "1", "2", "1", "n"]
        main()
        last_called = patched_print.call_count
        self.assertEqual(patched_print.call_args_list[last_called - 1][0][0],
                         "El juego ha terminado. Felicitaciones: Jugador 1, has ganado")

    def test_row(self, patched_input, patched_print, *args):
        patched_input.side_effect = ["x", "y", "1", "1", "2", "2", "3", "3", "4", "n"]
        main()
        last_called = patched_print.call_count
        self.assertEqual(patched_print.call_args_list[last_called - 1][0][0],
                         "El juego ha terminado. Felicitaciones: Jugador 1, has ganado")

if __name__ == '__main__':
    unittest.main()
