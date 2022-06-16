from random import random
class Student():
    def __init__(self, id, name):
        self.studentid = id
        self.studentname = name
        self.attendance = []

    def __init__(self, id):
        self.studentid = id
        self.studentname = random()
        self.attendance = []

    def addAttendance(self):
        self.attendance.append(1)

    def addAbsence(self):
        self.attendance.append(0)

    def modifyAttendance(self):
        self.attendance[-1] = 0

    def getWeeklyAttendance(self):
        if len(self.attendance) % 5 == 0 and len(self.attendance) > 0:
            substr = self.attendance[-5:]
            sum = 0
            for x in substr:
                sum = sum + x
                print(x)
            print("This week's attendance = 5 days, {0:.0%}".format(float(sum / 5)))
        elif len(self.attendance) > 0:
            temp = len(self.attendance) % 5
            sum = 0
            for x in self.attendance[-temp:]:
                sum = sum + x
            print(f"This week's attendance = {temp} days,", " {0:.0%}".format(float(sum / temp)))
        else:
            print("No records yet!")

    def getMonthlyAttendance(self):
        if len(self.attendance) % 5 == 0:
            sum = 0
            for x in self.attendance[-20:]:
                sum = sum + x
            print("This month's attendance = 4 weeks {0:.0%}".format(float(sum / 20)))
        else:
            temp = len(self.attendance) % 5
            sum = 0
            for x in self.attendance[-(temp + 15):]:
                sum = sum + x
            print(f"This month's attendance = 3 weeks and {temp} days,", "{0:.0%}".format(float(sum / (temp + 15))))

    def getYearlyAttendance(self):
        if len(self.attendance) > 0:
            result = sum(self.attendance)
            months = 0
            weeks = 0
            if len(self.attendance) >= 20:
                months = len(self.attendance) // 20
            if len(self.attendance) >= 5:
                weeks = (len(self.attendance) % 20) // 5
            days = (len(self.attendance) % 20) % 5
            print(f"This year's attendance = {months} month(s), {weeks} week(s) and {days} days,"," {0:.0%}".format(float(result / len(self.attendance))))
        else:
            print("No records for the year!")