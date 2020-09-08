import os

link: str = "C:\\Users\\User\Desktop\osTest"


# print(os.getcwd())



def app(str1: str):
    os.chdir(str1)
    name: int = 1
    for file in os.listdir(str1):
        print(file)
        src = os.path.abspath(file)
        dst = str1 + '\\' + str(name) + "." + os.path.basename(file).split(".")[-1]
        print(src)
        print(dst)

        os.rename(src, dst)
        name += 1
        print(name)


app(input())
