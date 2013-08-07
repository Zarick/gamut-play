
import unittest
import io
import console

class BasicFunctionality(unittest.TestCase):

    def test_default_prompt(self):
        input = io.StringIO("quit")
        output = io.StringIO()
        c = console.Console(stdin=input, stdout=output)
        c.use_rawinput = False
        c.start()
        self.assertEqual(output.getvalue(), "[gamut] ")


if __name__ == '__main__':
    unittest.main()
