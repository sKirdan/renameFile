import os
import re

regex: str = "(_%s)(\W|_)"

link: str = "C:\\Users\\User\Desktop\dd"
namePattern: str = input()
language: [] = [
    "es-mx", "zh-hans", "zh-hant", "zh-cn", "bg", "ch", "cs", "da",
    "es", "et", "fi", "fr", "hu", "it", "ja", "ko",
    "ms", "no", "nl", "pl", "pt", "ro",
    "ru", "sk", "sv", "th", "de", "el", "en",
]


def renameFiles(address: str, namePattern: str):
    os.chdir(address)
    collectTypes()


def collectTypes():
    for file in os.listdir(os.getcwd()):
        print(file)
        if not os.path.isdir(file):

            for abbr in language:
                file = file.lower()
                if re.search(regex % abbr, file):
                    splitedName = re.split(regex % abbr, file)
                    splitedName[0] = namePattern
                    tmpName: str = ""
                    os.rename(os.path.abspath(file), os.getcwd() + '\\' + str.join(tmpName, splitedName))
                    print(file)
                    print(splitedName)


renameFiles(link, namePattern)
