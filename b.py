mport re
from abc import ABC, abstractmethod
 
class Validator(ABC):
    def __set_name__(self, owner, name):
        self.name = name
        
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, None)
 
    @abstractmethod
    def __set__(self, instance, value):
        ...
 
class StringValidator(Validator):
    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError("Must be a string")
        if not value.strip():
            raise ValueError("String cannot be empty")
        return True
 
    def __set__(self, instance, value):
        if self.validate(value):
            instance.__dict__[self.name] = value
 
class ContactValidator(Validator):
    def validate_phone_number(self, phone_number):
        if not phone_number:
            raise ValueError("Phone number cannot be empty")
        pattern = r"^(?:\+374|0)(10|11|33|41|43|44|55|77|91|93|94|95|96|98|99)\d{6}$"
        if not re.match(pattern, phone_number):
            raise ValueError("Invalid phone number format")
        return True
 
    def __set__(self, instance, value):
        if self.validate_phone_number(value):
            instance.__dict__[self.name] = value
