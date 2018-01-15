import sys


def getNameOfFileToHighlight():
    return sys.argv[-1]


def loadListOfWordsToHighlight():
    listOfWords = []
    with open('listOfWords.txt', 'r') as file:
        content = file.readlines()
        for word in content:
            listOfWords.append(str(word).replace("\n", ""))
    capitalizedWords = []
    for word in listOfWords:
        capitalizedWords.append(word.title())
    listOfWords += capitalizedWords
    return listOfWords


def main():
    nameOfInputFile = getNameOfFileToHighlight()
    listOfWords = loadListOfWordsToHighlight()
    print(listOfWords)
    with open(nameOfInputFile, 'r+') as file:
        content = file.read()
        print(type(content))
        for word in listOfWords:
            content=content.replace(" " + word + " ", " \\textit{" + word + "} ")
            content=content.replace(" " + word + ",", " \\textit{" + word + "},")
            content=content.replace(" " + word + ")", " \\textit{" + word + "})")
            content=content.replace("(" + word + ")", "(\\textit{" + word + "})")
            content=content.replace("." + word + " ", ".\\textit{" + word + "} ")
            content=content.replace("." + word + " ", ".\\textit{" + word + "} ")
            content=content.replace(" " + word + ".", " \\textit{" + word + "}.")
            print(" " + word + " ")
        newFile = open('myfile.tex', 'w+')
        print(content)
        for line in content:
            newFile.write(line)


if __name__ == "__main__":
    main()
