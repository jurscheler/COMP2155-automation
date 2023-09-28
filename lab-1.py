class Student:
    def __init__(self, firstname, lastname, studentnr):
        self.firstname = firstname
        self.lastname = lastname
        self.studentnr = studentnr

    def __str__(self):
        return f"Firstname: {self.firstname}\nLastname: {self.lastname}\nStudent's number: {self.studentnr}"

    def writeToFile(self):
        filename = self.studentnr + ".txt"
        with open(filename, "w") as f:
            f.write(self.firstname + "\n")
            f.write(self.lastname + "\n")

firstname = input("Enter your first name: ")
lastname = input("Enter your last name: ")
studentNumber = input("Enter your student number: ")
s = Student(firstname, lastname, studentNumber)
print(s)
s.writeToFile()

with open(studentNumber + ".txt", "r") as f:
    fname = f.readline().strip()
    lname = f.readline().strip()
    print(f"The student firstname is {fname}. The student lastname is {lname}")
