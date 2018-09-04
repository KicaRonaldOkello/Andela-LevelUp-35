import unittest
from SignUp import Register

class TestSignUp(unittest.TestCase):
    def setUp(self):
        self.register = Register()
        self.a = len(self.register.details)

    def test_create_register(self):
        self.assertIsInstance(self.register, Register)



    def test_firstName(self):
       
        self.register.firstName("kica")
        self.assertEqual(len(self.register.details), self.a)

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

    def test_confirm(self):
        a = len(self.register.REGISTER)
        self.register.firstName("kica")
        self.register.lastName("ronald")
        self.register.emails("okello.ronald@gmail.com")
        self.register.confirm()
        self.assertEqual(len(self.register.REGISTER), a+1)

    def test_length_of_register_list(self):
        pass
        
        