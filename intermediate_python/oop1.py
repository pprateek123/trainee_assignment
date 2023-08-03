class University:
    def __init__(self, name, location):
        self._name = name
        self._location = location
        self._departments = []

    def add_department(self, department):
        self._departments.append(department)

    def display_details(self):
        print(f"University: {self._name}")
        print(f"Location: {self._location}")
        print("Departments:")
        for department in self._departments:
            print(f" - {department.get_department_name()}")

class Department(University):
    def __init__(self, name, location, department_name, hod):
        super().__init__(name, location)
        self._department_name = department_name
        self._hod = hod
        self._courses = []

    def add_course(self, course):
        self._courses.append(course)

    def get_department_name(self):
        return self._department_name

    def display_details(self):
        super().display_details()
        print(f"Department: {self._department_name}")
        print(f"Head of Department: {self._hod}")
        print("Courses offered:")
        for course in self._courses:
            print(f" - {course}")


university = University("Trubhuwan University", "Kirtipur")
department = Department("kathmandu  University", "dhulikel", "Computer Science", "Dr.sad")
department.add_course("Introduction to Programming")
department.add_course("Data Structures")


university.display_details()
print("\n")
department.display_details()