from math import ceil
from Section import *


class Year:
    def __init__(self, yearName):
        self.Sections = []
        self.yearName = yearName

    def populate(self, studentIdentifier, numberOfStudents, sectionSize):
        numOfSections = ceil(numberOfStudents / sectionSize)
        letter = 'A'
        for i in range(numOfSections):
            if numberOfStudents % 20 == 0:
                size = 20
            else:
                if i != numOfSections - 1:
                    size = 20
                else:
                    size = numberOfStudents % 20
            self.Sections.append(Section(sectionSize, letter))
            self.Sections[i].naivepopulate(studentIdentifier + (i * sectionSize), size)
            i = ord(letter[0])
            i += 1
            letter = chr(i)

    def mockTakeAttendance(self, section):
        if section - 1 < len(self.Sections):
            self.Sections[section - 1].mockAttendance()
        else:
            print("Invalid section present")

    def mockTakeAbsence(self, section):
        if section - 1 < len(self.Sections):
            self.Sections[section - 1].mockAbsent()
        else:
            print("Invalid section absent")

    def addSection(self):
        size = len(self.Sections)
        letter = 'A'
        i = ord(letter[0])
        i += size
        letter = chr(i)
        self.Sections.append(Section(20, letter))

    def addStudent(self, name):
        sum = 0
        for x in self.Sections:
            sum += len(x.Students)
            print("Sum = ", sum)
        if sum > 100:
            raise IndexError("Student limit reached for this year")
        else:
            lastid = self.Sections[-1].Students[-1].studentid
            print("last id = ", lastid)
            newid = lastid + 1
            studentOb = Student(newid)
            if len(self.Sections[-1].Students) == 20:
                self.addSection()
                print("New Section made!")
                self.Sections[-1].Students.append(studentOb)
            else:
                self.Sections[-1].Students.append(studentOb)

            lastid = self.Sections[-1].Students[-1].studentid
            print("last id = ", lastid)

