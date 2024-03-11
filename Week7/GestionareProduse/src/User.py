class User:
    def __init__(self, user_id, name, email, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.__validate_password(password)  # nu dorim sa accesam password in afara si nu e nevoie de self

        # folosim list compreh. pt a genera o secventa de valori True sau False

    def __validate_password(self, password):
        if any(char.isupper() for char in password) \
                and any(char.isdigit() for char in password) \
                and len(password) > 7:
            self.__password = password
        else:
            raise ValueError("Invalid password! The password must contain at least one uppercase letter, one digit, \
            and be at least 7 characters long.")
        return "Password created"
