acceptableCredits = [0, 20, 40, 60, 80, 100, 120]

progressCount = 0
trailerCount = 0
retrieverCount = 0
excludedCount = 0

progressList = []
trailerList = []
retrieverList = []
excludedList = []

progressionList = [
    "Progress",
    "Progress (module trailer)",
    "Module retriever",
    "Exclude"
]

creditList = {
    progressionList[0]: progressList,
    progressionList[1]: trailerList,
    progressionList[2]: retrieverList,
    progressionList[3]: excludedList
}

creditListWithStudents = {
    progressionList[0]: {},
    progressionList[1]: {},
    progressionList[2]: {},
    progressionList[3]: {}
}

creditListFile_r = open('Credit_List_File.txt', 'r')
creditListFile_w = open('Credit_List_File.txt', 'a')


def validate(creditsToValidate):
    if creditsToValidate not in acceptableCredits:
        print("Out of range")
        return False

    return True


while True:
    try:
        studentId = input("Enter student ID: ").lower()
        if studentId == '' or studentId[0] != "w" or len(studentId) != 8:
            print("Student ID is not valid")
            continue

        passCredits = int(input("Enter your total PASS credits: "))
        if not validate(passCredits):
            continue

        deferCredits = int(input("Enter your total DEFER credits: "))
        if not validate(deferCredits):
            continue

        failCredits = int(input("Enter your total FAIL credits: "))
        if not validate(failCredits):
            continue

    except ValueError:
        print("Integer required \n")
        continue

    totalCredits = passCredits + deferCredits + failCredits
    if totalCredits != 120:
        print("Total Incorrect")
        continue

    fileWriteFormat = "%s - %d, %d, %d \n"
    currentCredits = "%d, %d, %d" % (passCredits, deferCredits, failCredits)

    if passCredits == 120:
        print("Progress")
        progressCount += 1
        progressList.append(currentCredits)
        creditListFile_w.write(fileWriteFormat % (progressionList[0], passCredits, deferCredits, failCredits))
        creditListWithStudents[progressionList[0]][studentId] = currentCredits

    elif passCredits == 100:
        print("Progress (module trailer)")
        trailerCount += 1
        trailerList.append(currentCredits)
        creditListFile_w.write(fileWriteFormat % (progressionList[1], passCredits, deferCredits, failCredits))
        creditListWithStudents[progressionList[1]][studentId] = currentCredits

    elif failCredits > 60:
        print("Exclude")
        excludedCount += 1
        excludedList.append(currentCredits)
        creditListFile_w.write(fileWriteFormat % (progressionList[3], passCredits, deferCredits, failCredits))
        creditListWithStudents[progressionList[3]][studentId] = currentCredits

    else:
        print("Module Retriever")
        retrieverCount += 1
        retrieverList.append(currentCredits)
        creditListFile_w.write(fileWriteFormat % (progressionList[2], passCredits, deferCredits, failCredits))
        creditListWithStudents[progressionList[2]][studentId] = currentCredits

    choice = ''
    while True:
        print("\nWould you like to enter another set of data?")
        choice = input("Enter 'y' for yes or 'q' to quit and view results: ")

        if choice == 'y' or choice == 'Y' or choice == 'q' or choice == 'Q':
            break

    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n")
    if choice == 'q' or choice == 'Q':
        break

print()
print("Part I ------------------------------------------------------------")
print("Histogram")

txt = "%s \t %3d  : %s "
print(txt % ("Progress", progressCount, '*' * progressCount))
print(txt % ("Trailer", trailerCount, '*' * trailerCount))
print(txt % ("Retriever", retrieverCount, '*' * retrieverCount))
print(txt % ("Excluded", excludedCount, '*' * excludedCount))

print("\n%d outcomes in total." % (progressCount + trailerCount + retrieverCount + excludedCount))
print("-------------------------------------------------------------------")

# Part II

print()
print("Part II -----------------------------------------------------------")

for index, cList in enumerate(creditList.values()):
    for item in cList:
        txt = "%s - %s" % (progressionList[index], item)
        print(txt)

    print()

print("-------------------------------------------------------------------")

# Part III

print()
print("Part III ----------------------------------------------------------")

line = creditListFile_r.readline()
while line:
    print(line.strip())
    line = creditListFile_r.readline()

print("-------------------------------------------------------------------")

# Part IV

print()
print("Part IV ------------------------------------------------------------")

for name in progressionList:
    print(name, ":")
    studentList = creditListWithStudents[name]

    for student in studentList:
        print("%s : %s" % (student, studentList[student]))

    print()

print("-------------------------------------------------------------------")
