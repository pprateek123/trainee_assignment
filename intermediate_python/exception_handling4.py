class InvalidAgeError(Exception):
    def __init__(self, age):
        super().__init__(f"InvalidAgeError: Age '{age}' is not within the valid range (0 to 120).")

   
age = int(input('enter age: '))
if age>0 and age<120:
    print(age)
else:
    raise InvalidAgeError


