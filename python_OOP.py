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
