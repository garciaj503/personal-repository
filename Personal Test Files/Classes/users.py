class User:
    def __init__(self, first_name, last_name, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
    
    def describe_user(self):
        print(f"""Name: {self.first_name}
Last Name: {self.last_name}
Email: {self.email}
Phone Number: {self.phone_number}""")
        
    def greet_user(self):
        print(f"Welcome, {self.first_name}!")
        
#Creating instance 1 for user 1
user1 = User("Jaime", "Garcia", "jagarcia767.jr@gmail.com", "908-449-6458")
user1.describe_user()
user1.greet_user()

print()

#Creating instance 2 for user 2
user2 = User("Fatima", "Escobar", "escobar.2305@gmail.com", "503-70677919")
user2.describe_user()
user2.greet_user()

print()

#Creating instance 3 for user 3
user3 = User("Eliam", "Garcia", "eliamga48@gmail.com", "908-445-3489")
user3.describe_user()
user3.greet_user()