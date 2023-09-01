import unittest
from solution import parse_config

class TestSolution(unittest.TestCase):
    expected0 = {
        'section': {'b': False, 'f': 206.201, 'i': -55, 'i1': 1, 'b1': True, 'b2': False, 's': ''}
    }

    expected1 = {
        'owner': {'name': 'John Doe', 'organization': 'Acme Widgets Inc.', 'active': True, 'rate': 2.03},
        'database': {'server': '192.0.2.62', 'port': 143, 'file': '"payroll.dat"', 'connection': ''}
    }

    def test_parse_config(self):
        self.assertDictEqual(parse_config('data/generic.ini'), self.expected0)
        self.assertDictEqual(parse_config('data/sample.ini'), self.expected1)


if __name__ == '__main__':
    unittest.main()
