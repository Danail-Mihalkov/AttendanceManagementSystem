from Student import *

class Section:

    def __init__(self, size, name):
        self.size = size
        self.Students = []
        self.staff = None
        self.name = name

    def allocateStaff(self, staffObject):
        self.staff = staffObject

    def populate(self):
        for i in range(self.size):
            id = int(input("Enter id "))
            temp = Student(id)
            self.Students.append(temp)

    def naivepopulate(self,id, numStudents):
        for i in range(numStudents):
            temp = Student(id+i)
            self.Students.append(temp)

    def addStudent(self):
        self.Students.append(Student())

    def takeAttendance(self):
        for x in self.Students:
            x.addAttendance()
        temp = input("Are there absent students? Y/N ")
        if temp == "Y":
            print("When finished type '0'")
            studentid = int(input("Enter student ID "))
            while studentid != 0:
                mapstudents = map(lambda t: (t.studentid), self.Students)
                studentIDs = list(mapstudents)
                while studentid not in studentIDs:
                    studentid = int(input("Invalid ID, Enter student ID "))
                filters_students = filter(lambda x: (x.studentid == studentid), self.Students)
                student = list(filters_students)
                student[0].modifyAttendance()
                studentid = int(input("Enter student ID "))
        self.display()


    def mockAttendance(self):
        for x in self.Students:
            x.addAttendance()

    def mockAbsent(self):
        for x in self.Students:
            x.addAbsence()


    def printAttendance(self):
        for x in self.Students:
            print(x.attendance)

    def display(self):
        present = 0
        absent = 0
        for x in self.Students:
            if x.attendance[-1] == 1:
                present += 1
            else:
                absent += 1
        print("Number of students present today = ", present)
        print("Number of students absent today = ", absent)
        print("Total students = ", absent + present)

    def getWeeklyAttendance(self, id):
        found = False
        for x in self.Students:
            if x.studentid == id:
                x.getWeeklyAttendance()
                found = True
                break
        if (not found):
            raise NameError("Invalid Student ID")

    def getMonthlyAttendance(self, id):
        if len(self.Students[0].attendance) < 20:
            raise ValueError("Not enough records to create monthly sheet")
        else:
            found = False
            for x in self.Students:
                if x.studentid == id:
                    x.getMonthlyAttendance()
                    found = True
                    break
            if (not found):
                raise NameError("Invalid Student ID")

    def getYearlyAttendance(self, id):
        found = False
        for x in self.Students:
            if x.studentid == id:
                x.getYearlyAttendance()
                found = True
                break
        if (not found):
            raise NameError("Invalid Student ID")