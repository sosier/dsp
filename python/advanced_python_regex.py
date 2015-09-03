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


def histogram(ls):
    hist = dict()
    for item in ls:
        hist[item] = hist.get(item, 0) + 1

    return hist


def printQuestionResponse(descriptor, results):
    print("There are %d different %s:" % (len(results), descriptor))

    resultsTup = results.items()
    resultsTup = sorted(resultsTup, key=lambda x: x[1], reverse=1)
    n = 1
    for item in resultsTup:
        print(" %d. %s = %d" % (n, item[0], item[1]))
        n += 1


facultyData = read_data("python/faculty.csv")
headers = facultyData[0]
degree_i = headers.index(" degree")
title_i = headers.index(" title")
email_i = headers.index(" email")

# Q1
rawDegreeList = [x[degree_i] for x in facultyData[1:]]
rawDegreeListStr = " ".join(rawDegreeList)
rawDegreeListStr = re.sub(r"[\.0]", r"", rawDegreeListStr)
degreeList = re.findall(r"\w+", rawDegreeListStr)
degreeResults = histogram(degreeList)
printQuestionResponse("degrees", degreeResults)

# Q2
rawTitleList = [x[title_i] for x in facultyData[1:]]
rawTitleListStr = "||".join(rawTitleList)
rawTitleListStr = re.sub(r" (of|is) Biostatistics", r"", rawTitleListStr)
titleList = rawTitleListStr.split("||")
titleResults = histogram(titleList)
printQuestionResponse("titles", titleResults)

# Q3 (not sure if this is cheating b/c it doesn't use a regex)
emailList = [x[email_i] for x in facultyData[1:]]
print(emailList)

# Q4
emailListStr = " ".join(emailList)
emailDomainList = re.findall(r"\w+@(\w+\.[\w.]+)", emailListStr)
emailDominResults = histogram(emailDomainList)
printQuestionResponse("email domains", emailDominResults)
