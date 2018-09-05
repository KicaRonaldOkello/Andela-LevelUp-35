


class Register:
    REGISTER = []
    details = {}

    def firstName(self, firstname):
        if firstname == "":
            return ("Please enter first name")
        else:
            self.details["firstname"] = firstname

    def lastName(self, lastname):
        if lastname == "":
            return ("Please enter last name")
        else:
            self.details["lastname"] = lastname

    def emails(self, email):
        if email == "":
            return ("Please enter valid email")
        else:
            self.details["email"] = email
        

    def confirm(self):
        if len(self.details) !=  0:
            self.REGISTER.append(self.details)
            print ("Entry confirmed")
            print ("there are " + str(len(self.REGISTER)) + " users")
        else:
            print ("Error in registration")

#sign = Register()
#sign.firstName("Kica")
#sign.lastName("ROnald")
#sign.emails("okello.ronald@gmail.com")
#sign.confirm()



