import unittest
from test_simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Test class for SimpleCalculator"""

    def setUp(self):
        self.calc = SimpleCalculator()

