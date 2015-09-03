import csv
import re


def read_data(data):
    parsed = []

    f = open(data, "r")
    try:
        reader = csv.reader(f)
        for row in reader:
            parsed.append(row)
    finally:
        f.close()

    return parsed


def printDictItems(dictionary, numItems):
    itemsPrinted = 0
    for item in dictionary:
        if itemsPrinted < numItems:
            print(str(item) + ": " + str(dictionary[item]))
            itemsPrinted += 1
        else:
            return


facultyData = read_data("python/faculty.csv")
headers = facultyData[0]
data = facultyData[1:]
name_i = headers.index("name")
degree_i = headers.index(" degree")
title_i = headers.index(" title")
email_i = headers.index(" email")

# Q6
faculty_dict = dict()
for person in data:
    lastName = person[name_i].split(" ")[-1]
    degree = re.sub(r"[\.0]|^\s", r"", person[degree_i])
    title = re.sub(r" (of|is) Biostatistics", r"", person[title_i])
    email = person[email_i]
    faculty_dict[lastName] = faculty_dict.get(lastName, [])
    faculty_dict[lastName].append([degree, title, email])

printDictItems(faculty_dict, 3)

# Q7
professor_dict = dict()
for person in data:
    firstName = person[name_i].split(" ")[0]
    lastName = person[name_i].split(" ")[-1]
    nameTup = (firstName, lastName)
    degree = re.sub(r"[\.0]|^\s", r"", person[degree_i])
    title = re.sub(r" (of|is) Biostatistics", r"", person[title_i])
    email = person[email_i]
    professor_dict[nameTup] = [degree, title, email]

printDictItems(professor_dict, 3)

# Q8
unsortedProfessorDict = professor_dict.items()
sortedProfessorDict = sorted(unsortedProfessorDict, key=lambda x: x[0][1])
for i in range(3):
    print(str(sortedProfessorDict[i][0]) + ": " +
          str(sortedProfessorDict[i][1]))
