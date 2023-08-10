from flask import render_template


class User:
    def __init__(self, free, name, email, password, positionUser="User"):
        try:
            freeInt = int(free)
            if name == '' or email == '' or password == '':
                raise ValueError("Name, email, and password must not be empty")
        except ValueError:
            raise ValueError("Invalid value for 'free' or empty fields")

        self.free = freeInt
        self.name = name
        self.email = email
        self.password = password
        self.userPosition = positionUser

    @classmethod
    def from_position(cls, free, name, email, password, positionUser):
        return cls(free, name, email, password, positionUser)

    def validatePassword(self, inputPassword):
        return self.password == inputPassword
    def validadeFree(self,free):
        return self.free == free
