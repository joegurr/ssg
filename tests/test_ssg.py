import unittest

from ssg.core import generate


class TestSSG(unittest.TestCase):
    def test_simple_content(self):
        output = generate('./tests/simple_content.txt', False)
        with open('./tests/simple_content.html', 'r') as f:
            expected_result = ''.join(f.readlines())
        self.assertEqual(output, expected_result)

    def test_complex_content(self):
        output = generate('./tests/complex_content.txt', False)
        with open('./tests/complex_content.html', 'r') as f:
            expected_result = ''.join(f.readlines())
        self.assertEqual(output, expected_result)