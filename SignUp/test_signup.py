import unittest
from SignUp import Register

class TestSignUp(unittest.TestCase):
    def setUp(self):
        self.register = Register()
        self.a = len(self.register.details)

    def test_firstName(self):
       
        self.register.firstName("kica")
        self.assertEqual(len(self.register.details), self.a+1)

    def test_lastName(self):
        self.register.lastName("ronald")
        self.assertEqual(len(self.register.details), self.a+1)

    def test_emails(self):
        self.register.emails("okello.ronald@gmail.com")
        self.assertEqual(len(self.register.details), self.a+1)

    def test_whitespace(self):
        e = ""
        self.register.firstName(e)
        self.register.firstName(e)
        self.register.firstName(e)
        self.assertEqual(len(self.register.details), self.a)
        
