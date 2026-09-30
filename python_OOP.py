# Example 1
class Owner:
    def __init__(self, in_name, in_contact):
        self.name = in_name
        self.contact = in_contact


class Dog:
    def __init__(self, in_name, in_breed, in_owner=None):
        self.name = in_name
        self.breed = in_breed
        self.owner = in_owner

    def bark(
        self,
    ):
        # This method requires an instance of the class to be called
        print(f" Hello I am {self.name}, Woof")


owner1 = Owner("Alice", "alice@example.com")
owner2 = Owner("Bob", "bob@example.com")

dog1 = Dog(
    "Buddy", "Golden Retriever", owner1
)  # Having another object as an attribute of another object
dog2 = Dog("Max", "German Shepherd")

# print(dog1.owner.name)
# print(dog2.owner)  # This will print None since dog2 has no owner assigned
print(dog2.bark())


# Example 2
class User:
    def __init__(self, in_username, in_email, in_password):
        self.username = in_username
        self._email = in_email  # protected attribute/variable single underscore
        self.password = in_password

    # getter property for email
    @property
    def email(self):  # email is now a method that can be accessed like an attribute
        return self._email

    # setter property for email
    @email.setter
    def email(self, new_email):
        if ".com" in new_email:
            self._email = new_email
        else:
            raise ValueError("Invalid email address")

    def say_hi(self, input_user):
        print(f"Hello, {input_user.username}! My name is {self.username}.")


user1 = User("Alice", "alice@example.com", "123")
user2 = User("Bob", "bob@example.com", "456")

user1.say_hi(user2)  # This will print: Hello, Bob! My name is Alice.

print(user1.username)
user1.username = "Alice Smith"  # Modifying works cause not protected

print(user1.email)
# user1.email = "new email"  #This now goes through the setter method cause email is protected


# Example 3
class Student:
    # Static attribute (class attribute). static attribute means it is common/shared across all instances of the class
    # and it is not tied to any specific instance of the class. It belongs to the class itself.
    school_name = "ABC High School"
    student_count = 0

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute
        Student.student_count += 1

    # Static method
    # Static methods are methods that belong to the class rather than an instance of the class.
    # They do not have access to instance-specific data (like self) and can be called on the class itself or on instances of the class.

    @staticmethod
    def is_adult(age):
        return age >= 18


# Create objects
student1 = Student("Alice", 20)
student2 = Student("Bob", 16)
print(Student.student_count)  # Output: 2

# Access the static/class attribute
# it is not recommended to access static attributes through instances of the class
print(Student.school_name)
print(student1.school_name)
print(student2.school_name)

# Use the static method either on class or instance of the class
print(Student.is_adult(20))  # True
print(Student.is_adult(16))  # False
print(student1.is_adult(student1.age))  # True


# Example 4 - Encapsulation
class BadBankAccount:
    def __init__(self, in_balance):
        self.balance = in_balance


account1 = BadBankAccount(0.0)
account1.balance = -100  # This is not good, we should not allow negative balance


class GoodBankAccount:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        # break exits a loop.
        # raise signals an error and unwinds out of the current function
        # ValueError: the function got a value it can’t accept
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount


account2 = GoodBankAccount()
print(account2.balance)  # Output: 0
# account2.balance = 100  # This will raise an AttributeError since we dont have a setter for balance
account2.deposit(199)
account2.withdraw(50)
print(account2.balance)  # Output: 149


# Example 5 - protected methods
class BaseClass:
    def __init__(self):
        self._protected_attribute = "I am protected"

    def _protected_method(self):
        print("This is a protected method")

    # protected methods are not meant to be accessed from outside the class,
    # they are usllay used inside the class or by subclasses to provide functionality that is not intended to be part of the public interface of the class.


# Example 6 - abstaction
class EmailService:
    def connect(self):
        print("Connecting to email server...")

    def authenticate(self):
        print("Authenticating...")

    def send_email(self):
        print("Sending email...")


service1 = EmailService()
service1.connect()
service1.authenticate()
service1.send_email()


class AbstractEmailService:
    def _connect(self):
        print("Connecting to email server...")

    def _authenticate(self):
        print("Authenticating...")

    def send_email(self):
        self._connect()
        self._authenticate()
        print("Sending email...")


service2 = AbstractEmailService()
service2.send_email()  # This will call the protected methods internally


# Example 7 - Inheritance
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print("engine started.")


class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)  # Call the constructor of the parent class
        self.num_doors = num_doors

    def start_engine(self):
        print(
            f"{self.make} {self.model} car engine started with {self.num_doors} doors."
        )


class Bike(Vehicle):
    def __init__(self, make, model, has_pedals):
        super().__init__(make, model)  # Call the constructor of the parent class
        self.has_pedals = has_pedals

    def start_engine(self):
        print(
            f"{self.make} {self.model} bike engine started. Pedals: {self.has_pedals}"
        )


car1 = Car("Toyota", "Camry", 4)
bike1 = Bike("Yamaha", "YZF-R3", False)
print(car1.__dict__)  # Output: {'make': 'Toyota', 'model': 'Camry', 'num_doors': 4}
print(
    bike1.__dict__
)  # Output: {'make': 'Yamaha', 'model': 'YZF-R3', 'has_pedals': False}

car1.start_engine()  # Output: Toyota Camry car engine started with 4 doors.
bike1.start_engine()  # Output: Yamaha YZF-R3 bike engine started. Pedals: False
