import glob


listOfSQLKeywords = []
for line in open("SQLkeywords.txt", "r"):
    listOfSQLKeywords.append(line.strip())

def convertToCapital(listOfLines):

    wordCount = len(listOfSQLKeywords)
    for i in range(wordCount):
        listOfSQLKeywords.append("(" + listOfSQLKeywords[i])

    newListOfLines = []

    for i in range(len(listOfLines)):
        listOfWords = listOfLines[i].strip().split()
        newListOfWords = []
        newString = ""

        for i in range(len(listOfWords)):
            if listOfWords[i].lower() in listOfSQLKeywords:
                newString += listOfWords[i].upper() + " "
            else:
                newString += listOfWords[i] + " "
        
        newString = newString.strip() + "\n"

        newListOfLines.append(newString)
        

    return newListOfLines

for filename in glob.glob("*.sql"):
    infile = open(filename, "r")
    newFile = convertToCapital(infile.readlines())
    infile.close()
    outfile = open(filename, "w")
    outfile.writelines(newFile)