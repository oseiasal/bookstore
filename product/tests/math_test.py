from django.test import TestCase


class MathTestCase(TestCase):
    def test_addition(self):
        result = 1 + 1
        self.assertEqual(result, 3)
