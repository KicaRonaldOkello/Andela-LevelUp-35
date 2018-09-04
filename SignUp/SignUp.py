


class Register:
    REGISTER = []
    details = {}

    def firstName(self, firstname):
        if firstname == "":
            print ("Please enter first name")
        else:
            self.details["firstname"] = firstname

    def lastName(self, lastname):
        if lastname == "":
            print ("Please enter lastname name")
        else:
            self.details["lastname"] = lastname

    def emails(self, email):
        if email == "":
            print ("Please enter valid email")
        else:
            self.details["email"] = email

    def confirm(self):
        self.REGISTER.append(self.details)
        if self.REGISTER is not None:
            print ("Entry confirmed")
            print ("there are " + str(len(self.REGISTER)) + " users")
        else:
            self.REGISTER.remove(-1)
            print ("Error in registration")

#sign = Register()
#sign.firstName("Kica")
#sign.lastName("ROnald")
#sign.emails("okello.ronald@gmail.com")
#sign.confirm()



