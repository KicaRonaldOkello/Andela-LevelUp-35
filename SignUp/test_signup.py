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
        self.assertEqual(self.register.details["firstname"], "kica")

    def test_lastName(self):
        self.register.lastName("ronald")
        self.assertEqual(self.register.details["lastname"], "ronald")

    def test_emails(self):
        self.register.emails("okello.ronald@gmail.com")
        self.assertEqual(self.register.details["email"], "okello.ronald@gmail.com")

    def test_empty_email(self):
        
        self.assertEqual(self.register.emails(""), "Please enter valid email")

    def test_empty_firstname(self):
       self.assertEqual(self.register.firstName(""), "Please enter first name") 

    def test_empty_lastname(self):
        self.assertEqual(self.register.lastName(""), "Please enter last name") 

    def test_whitespace(self):
        e = ""
        self.register.firstName(e)
        self.register.firstName(e)
        self.register.firstName(e)
        self.assertEqual(len(self.register.details), self.a)

    def test_length_of_register_list(self):
        a = len(self.register.REGISTER)
        self.register.firstName("kica")
        self.register.lastName("ronald")
        self.register.emails("okello.ronald@gmail.com")
        self.register.confirm()
        self.assertEqual(len(self.register.REGISTER), a+1)

    def test_confirm(self):
        e = ""
        self.register.firstName(e)
        self.register.lastName(e)
        self.register.emails(e)
        self.register.confirm()
        self.assertEqual(len(self.register.REGISTER), 0)
        
        
        
