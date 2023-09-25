import csv
import datetime
import os


def is_leap_year(year):
  if year % 400 == 0:
    return True
  elif year % 100 == 0:
    return False
  elif year % 4 == 0:
    return True
  else:
    return False


fields = ["Subject", "Start Date", "Start Time", "All Day Event", "Description"]

with open("calendar.csv", 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(fields)

    for i in os.listdir("/Users/colincannell/PycharmProjects/WorkoutApp/main/plan"):
        content = open(f"/Users/colincannell/PycharmProjects/WorkoutApp/main/plan/{i}").read().splitlines()
        subject = content[0]

        description = content[1::]

        for j in range(description.count('')):
            description.remove('')

        description = str.join("\n", description)

        print(description)

        today = datetime.date.today()
        weekday = today.weekday()
        day = today.day

        dt = datetime.datetime.now()
        year = dt.year
        month = dt.month

        '''
        monday 0
        tuesday 1
        wednesday 2
        thursday 3
        friday 4
        saturday 5
        sunday 6
        '''

        if weekday == 0:
            monday = 7
            tuesday = 8
            wednesday = 9
            thursday = 10
            friday = 11
        elif weekday == 1:
            monday = 6
            tuesday = 7
            wednesday = 8
            thursday = 9
            friday = 10
        elif weekday == 2:
            monday = 5
            tuesday = 6
            wednesday = 7
            thursday = 8
            friday = 9
        elif weekday == 3:
            monday = 4
            tuesday = 5
            wednesday = 6
            thursday = 7
            friday = 8
        elif weekday == 4:
            monday = 3
            tuesday = 4
            wednesday = 5
            thursday = 6
            friday = 7
        elif weekday == 5:
            monday = 2
            tuesday = 3
            wednesday = 4
            thursday = 5
            friday = 6
        elif weekday == 6:
            monday = 1
            tuesday = 2
            wednesday = 3
            thursday = 4
            friday = 5

        if i == "Day1 (Monday).txt":
            sDate = day + monday
        elif i == "Day2 (Tuesday).txt":
            sDate = day + tuesday
        elif i == "Day3 (Wednesday).txt":
            sDate = day + wednesday
        elif i == "Day4 (Thursday).txt":
            sDate = day + thursday
        elif i == "Day5 (Friday).txt":
            sDate = day + friday

        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10:
            if sDate > 31:
                sDate -= 31
                month += 1
        elif month == 2:
            if is_leap_year(year):
                if sDate > 29:
                    sDate -= 29
                    month += 1
        elif month == 4 or month == 6 or month == 9 or month == 11:
            if sDate > 30:
                sDate -= 30
                month += 1
        elif month == 12:
            if sDate > 31:
                sDate -= 31
                month = 1
                year += 1

        sDate = f"{month}/{sDate}/{year}"

        sTime = "12:00 AM"
        allDay = "TRUE"
        row = [subject, sDate, sTime, allDay, description]
        writer.writerow(row)




# monday
'''
7
8
9
10
11
12
'''

# tuesday
'''
6
7
8
9
10
'''

# wednesday
'''
5
6
7
8
9
'''

# thursday
'''
4
5
6
7
8
'''

# friday
'''
3
4
5
6
7
'''