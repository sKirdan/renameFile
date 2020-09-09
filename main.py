import os

link: str = ""


def organizeFolder(address: str):
    os.chdir(address)
    collectedTypes: {str: []} = collectTypes()

    createFoldersIfNotExist(collectedTypes.keys())
    groupByFolders(collectedTypes)


def collectTypes():
    folderTypes: {str: []} = {}
    for file in os.listdir(os.getcwd()):
        if not os.path.isdir(file):
            extension = file.split(".")[-1]
            if not folderTypes.get(extension):
                folderTypes[extension] = []
            folderTypes[extension].append(file)
    return folderTypes


def createFoldersIfNotExist(folders: [str]):
    for name in folders:
        if not os.path.exists(name):
            os.mkdir(name)


def groupByFolders(folder: {str: []}):
    for extension in folder.keys():
        for file in folder[extension]:
            src = os.path.abspath(file)
            dst = os.getcwd() + '\\' + extension + '\\' + str(file)
            os.rename(src, dst)


organizeFolder(link)
