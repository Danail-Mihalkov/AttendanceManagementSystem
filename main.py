from User import *
from Staff import *
"""
#listOfStaff = []
#listOfStaff.append(Staff(101, "staff1"))
#listOfStaff.append(Staff(102, "staff2"))


ob = Section(3)
ob.naivepopulate()
for i in range(0,23):
    ob.mockAttendance()

ob.printAttendance()
#ob.display()
#ob.getWeeklyAttendance(100)
#ob.getMonthlyAttendance(100)
ob.getYearlyAttendance(100)
"""


ob = User()
ob.populateYears()
for i in range (16):
    ob.Years[0].mockTakeAttendance(1)
for i in range (7):
    ob.Years[0].mockTakeAbsence(1)
ob.getWeeklyAttendance(1007)
ob.getMonthlyAttendance(1007)
ob.getYearlyAttendance(1007)
adminIDList = [111,222,333]
staff1 = Staff(1,"aaa")
staff2 = Staff(2,"bbb")
staff3 = Staff(3,"ccc")
staff4 = Staff(4,"ddd")
staff5 = Staff(5,"eee")
staffIDList = [staff1, staff2, staff3, staff4, staff5]
takenStaffList = []
while True:
    choice = int(input("1 Admin\n2 User\n3 Exit "))
    if choice == 1:
        staffID = int(input("Enter your staff ID "))
        while True:
            if staffID in adminIDList:
                ch = int(input("1 Add a student\n2 Allocate staff to a section\n3 Exit "))
                if ch == 1:
                    year = int(input("Enter year (1,2,3,4)"))
                    name = input("Enter Student name ")
                    try:
                        ob.Years[year - 1].addStudent(name)
                    except IndexError as e:
                        print(e)
                    else:
                        print(f"Student added successfully in section {ob.Years[year - 1].Sections[-1].name}!")
                elif ch == 2:
                    id = int(input("Enter staff ID "))
                    filters_staff = list(filter(lambda x: (x.ID == id), staffIDList))
                    filters_takenStaff = list(filter(lambda x: (x.ID == id), takenStaffList))
                    if len(filters_staff) > 0 and len(filters_takenStaff)==0:
                        name = filters_staff[0].Name
                        year = int(input("Enter year (1,2,3,4)"))
                        section = str(input("Enter section (A,B,C...)"))
                        ob.setStaff(Staff(id, name), year, section)
                        takenStaffList.append(filters_staff[0])
                elif ch == 3:
                    print(staffIDList)
                    print(takenStaffList)
                    break

            elif len(list(filter(lambda x: (x.ID == staffID), takenStaffList))) > 0:
                ch = int(input("1 Take attendance for your class\n2 Exit "))
                if ch == 1:
                    flag = False
                    for x in ob.Years:
                        for s in x.Sections:
                            if staffID == s.staff.ID:
                                s.takeAttendance()
                                flag = True
                                break
                        if flag:
                            break
                elif ch == 2:
                    break

    elif(choice == 2):
        studentid = int(input("Enter student id "))
        while True:
            ch = int(input("1 Weekly attendance\n2 Monthly attendance\n3 Yearly attendance\n4 Exit "))
            if ch == 1:
                try:
                    ob.getWeeklyAttendance(studentid)
                except IndexError as e:
                    print(e)


            elif ch == 2:
                try:
                    ob.getMonthlyAttendance(studentid)
                except IndexError as e:
                    print(e)
                except ValueError as e:
                    print(e)

            elif ch == 3:
                try:
                    ob.getYearlyAttendance(studentid)
                except IndexError as e:
                    print(e)

            elif ch == 4:
                break

    elif(choice == 3):
        break