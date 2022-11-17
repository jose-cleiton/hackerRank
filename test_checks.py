from unittest import TestCase, main
from checks import checks
from contextlib import redirect_stdout
import io


class Checks(TestCase):
    def test_its_pair(self):
        checks(2)

    def test_when_odd_returns_weird(self):
        input_value = 3
        expected_value = "Weird\n"
        f = io.StringIO()
        with redirect_stdout(f):
            checks(input_value)
        saida = f.getvalue()

        self.assertEqual(saida, expected_value)

    def test_when_even_and_between_2_and_5_returns_not_weird(self):
        input_value = 4
        expected_value = "Not Weird\n"

        f = io.StringIO()
        with redirect_stdout(f):
            checks(input_value)
        saida = f.getvalue()

        self.assertEqual(saida, expected_value)

    def test_when_even_e_between_2_and_5_returns_weird(self):
        input_value = 6
        expected_value = "Weird\n"
        f = io.StringIO()
        with redirect_stdout(f):
            checks(input_value)
        saida = f.getvalue()

        self.assertEqual(saida, expected_value)


main()
