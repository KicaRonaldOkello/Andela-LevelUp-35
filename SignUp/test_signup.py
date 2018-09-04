import unittest
from SignUp import Register

class TestSignUp(unittest.TestCase):
    def setUp(self):
        self.register = Register()

    def test_firstName(self):
        self.assertEqual(len(self.register.details), 0)
        self.register.firstName("kica")
        self.assertEqual(len(self.register.details), 1)

    def test_lastName(self):
        self.assertEqual(len(self.register.details), 1)
        self.register.lastName("ronald")
        self.assertEqual(len(self.register.details), 2)

    def test_zemails(self):
        self.assertEqual(len(self.register.details), 2)
        self.register.emails("okello.ronald@gmail.com")
        self.assertEqual(len(self.register.details), 3)