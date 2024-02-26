class User:

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.is_active = False

    def info(self):
        return f"name = {self.name} email = {self.email} is_active = {self.is_active}"

user1 = User(name="Vasya", email="kfd@dkj", password="hh")

print(user1.name)

user3 = User(name="Petay", email="hjhh@khgg", password="hfjh")
print(user3.info())


