class GuestList:
    USERS = []
        
    def adding_user(self, data):
        data["id"] = len(self.USERS) + 1
        self.USERS.append(data)
        return self.USERS

    def getting_user(self):
        return self.USERS

    def deleting_user(self):
        removed_user = self.USERS[-1]
        self.USERS.remove(removed_user)
        return removed_user