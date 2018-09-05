


class Register:
    REGISTER = []
    details = {}

    def firstName(self, firstname):
        """This method is used to input first name"""
        if firstname == "":
            return ("Please enter first name")
        else:
            self.details["firstname"] = firstname

    def lastName(self, lastname):
        """This method inputs last name."""
        if lastname == "":
            return ("Please enter last name")
        else:
            self.details["lastname"] = lastname

    def emails(self, email):
        """This method inputs email"""
        if email == "":
            return ("Please enter valid email")
        else:
            self.details["email"] = email


    def confirm(self):
        """This method inputs a user information and stores in list"""
        if len(self.details) != 0:
            self.REGISTER.append(self.details)
            print ("Entry confirmed")
            print ("there are " + str(len(self.REGISTER)) + " users")
        else:
            print ("Error in registration")





