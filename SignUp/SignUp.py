
REGISTER = []

class Register:
    details = []

    def firstName(self, firstname):
        if firstname == "":
            print ("Please enter first name")
        else:
            self.details.append(firstname)

    def lastName(self, lastname):
        if lastname == "":
            print ("Please enter lastname name")
        else:
            self.details.append(lastname)

    def emails(self, email):
        if email == "":
            print ("Please enter valid email")
        else:
            self.details.append(email)

    def confirm(self):
        REGISTER.append(self.details)
        if REGISTER is not None:
            print ("Entry confirmed")
        else:
            print ("Error in registration")



