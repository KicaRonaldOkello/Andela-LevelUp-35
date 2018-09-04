
REGISTER = []

class Register:
    details = []

    def firstName(self, firstname):

        self.details.append(firstname)

    def lastName(self, lastname):
        self.details.append(lastname)

    def emails(self, email):
        self.details.append(email)

    def confirm(self):
        REGISTER.append(self.details)
        if REGISTER is not None:
            print ("Entry confirmed")
        else:
            print ("Error in registration")



