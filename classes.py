class CareReceiver:
    def __init__(self, name: str, age: int, gender: str, address: str, phone_number: str, email: str):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.phone_number = phone_number
        self.email = email


    def __str__(self):
        return f"CareReceiver {self.name}, {self.age}, {self.gender}, {self.address}, {self.phone_number}, {self.email}"

    def __eq__(self, other: object) -> bool:
        return isinstance(other,
                          CareReceiver) and self.name == other.name and self.age == other.age and self.gender == other.gender and self.address == other.address and self.phone_number == other.phone_number and self.email == other.email

class CareGiver:
    def __init__(self, name: str, age: int, gender: str, address: str, phone_number: str, email: str):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"CareGiver {self.name}, {self.age}, {self.gender}, {self.address}, {self.phone_number}, {self.email}"

    def __eq__(self, other):
        return isinstance(other, CareGiver) and self.name == other.name and self.age == other.age and self.gender == other.gender and self.address == other.address and self.phone_number == other.phone_number and self.email == other.email
