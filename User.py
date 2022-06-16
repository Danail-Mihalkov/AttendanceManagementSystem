from Year import *
class User:
    def __init__(self):
        self.Years = []

    def populateYears(self):
        self.Years.append(Year("Year 1"))
        self.Years[0].populate(1000,80,20)

        self.Years.append(Year("Year 2"))
        self.Years[1].populate(2000, 90, 20)

        self.Years.append(Year("Year 3"))
        self.Years[2].populate(3000, 36, 20)

        self.Years.append(Year("Year 4"))
        self.Years[3].populate(4000, 30, 20)


    def getWeeklyAttendance(self, studentID):
        year = studentID // 1000
        numberOfStudents = studentID - (1000 * year)
        section = ceil(numberOfStudents / 20)
        if year > len(self.Years):
            raise IndexError("Incorrect student id. No such year in our records")
        if section > (len(self.Years[year].Sections)):
            print (len(self.Years[year]))
            raise IndexError("Incorrect student id. No such section for that year")

        if numberOfStudents < 20:
            self.Years[year - 1].Sections[0].getWeeklyAttendance(studentID)
        elif numberOfStudents < 40:
            self.Years[year - 1].Sections[1].getWeeklyAttendance(studentID)
        elif numberOfStudents < 60:
            self.Years[year - 1].Sections[2].getWeeklyAttendance(studentID)
        elif numberOfStudents < 80:
            self.Years[year - 1].Sections[3].getWeeklyAttendance(studentID)
        else:
            self.Years[year - 1].Sections[4].getWeeklyAttendance(studentID)

    def getMonthlyAttendance(self, studentID):
        year = studentID // 1000
        numberOfStudents = studentID - (1000 * year)
        section = ceil(numberOfStudents / 20)
        if year > len(self.Years):
            raise IndexError("Incorrect student id. No such year in our records")
        if section > (len(self.Years[year].Sections)):
            print(len(self.Years[year]))
            raise IndexError("Incorrect student id. No such section for that year")

        if numberOfStudents < 20:
            self.Years[year - 1].Sections[0].getMonthlyAttendance(studentID)
        elif numberOfStudents < 40:
            self.Years[year - 1].Sections[1].getMonthlyAttendance(studentID)
        elif numberOfStudents < 60:
            self.Years[year - 1].Sections[2].getMonthlyAttendance(studentID)
        elif numberOfStudents < 80:
            self.Years[year - 1].Sections[3].getMonthlyAttendance(studentID)
        else:
            self.Years[year - 1].Sections[4].getMonthlyAttendance(studentID)

    def getYearlyAttendance(self, studentID):
        year = studentID // 1000
        numberOfStudents = studentID - (1000 * year)
        section = ceil(numberOfStudents / 20)
        if year > len(self.Years):
            raise IndexError("Incorrect student id. No such year in our records")
        if section > (len(self.Years[year].Sections)):
            print(len(self.Years[year]))
            raise IndexError("Incorrect student id. No such section for that year")

        if numberOfStudents < 20:
            self.Years[year - 1].Sections[0].getYearlyAttendance(studentID)
        elif numberOfStudents < 40:
            self.Years[year - 1].Sections[1].getYearlyAttendance(studentID)
        elif numberOfStudents < 60:
            self.Years[year - 1].Sections[2].getYearlyAttendance(studentID)
        elif numberOfStudents < 80:
            self.Years[year - 1].Sections[3].getYearlyAttendance(studentID)
        else:
            self.Years[year - 1].Sections[4].getYearlyAttendance(studentID)

    def setStaff(self, staffObj, year, section):
        for x in self.Years:
            if x.yearName == (f"Year {year}"):
                for s in x.Sections:
                    if s.name == section:
                        s.allocateStaff(staffObj)