import random

weekdays = {"Day1 (Monday).txt": 'none', "Day2 (Tuesday).txt": 'none', "Day3 (Wednesday).txt": 'none', "Day4 (Thursday).txt": 'none', "Day5 (Friday).txt": 'none'}

workouts = ["arms", "lacrosse", "upper", "legs", "back"]


def checkMuscleGroupDup(workout, weekdays):
    if workout in weekdays.values():
        return False
    return True


for day in weekdays:
    workout = workouts[random.randint(0, len(workouts) - 1)]
    while not checkMuscleGroupDup(workout, weekdays):
        workout = workouts[random.randint(0, len(workouts) - 1)]
    weekdays[day] = workout


workouts = {"arms":["biceps", "triceps", "forearms"], "lacrosse":["lacrosse"],
            "upper":["chest", "shoulders", "deltoids"], "legs":["calves", "hamstrings", "quads"],
            "back":["back"]}


def checkExerciseDupe(exercise, exercises):
    for i in exercises:
        if i == f"{exercise}\n":
            return False
    return True


for day in weekdays:
    dayFilePath = f"/Users/colincannell/PycharmProjects/WorkoutApp/main/plan/{day}"
    exercises = [f"{weekdays[day]}/Abs\n\n"]

    for muscle in workouts[weekdays[day]]:
        muscleFilePath = f"/Users/colincannell/PycharmProjects/WorkoutApp/main/workouts/{weekdays[day]}/{muscle}.txt"
        muscleFile = open(muscleFilePath).read().splitlines()

        if muscle == "back" or muscle == "lacrosse":
            for i in range(3):
                for j in range(3):
                    exercise = random.choice(muscleFile)

                    while not checkExerciseDupe(exercise, exercises):
                        exercise = random.choice(muscleFile)

                    exercises.append(f"{exercise}\n")
                exercises.append("x2\n\n")
        else:
            for i in range(3):
                exercise = random.choice(muscleFile)

                while not checkExerciseDupe(exercise, exercises):
                    exercise = random.choice(muscleFile)

                exercises.append(f"{exercise}\n")
            exercises.append("x2\n\n")

    if weekdays[day] != "Lacrosse":
        exercises.append("Plank x1min\nSide Plank x45sec\nRussianTwists x70\nx2")

    with open(dayFilePath, 'w') as dayFile:
        dayFile.writelines(exercises)

dayFile.close()