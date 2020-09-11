import os
import re

regex: str = "(_%s[^a-zA-Z])"

link: str = "C:\\Users\\User\Desktop\dd"  # input()


class States:
    none: bool
    hovered: bool
    pressed: bool
    disabled: bool

    def str(self):
        return str(self.none) + " " + str(self.hovered) + " " + str(self.pressed) + " " + str(self.disabled)


statesList = ["none", "hovered", "pressed", "disabled"]
state = ["01", "02", "03", "04"]


def renameFiles(address: str, states: States):
    os.chdir(address)
    states = getCurrentStates(states)
    for file in os.listdir(os.getcwd()):
        if not os.path.isdir(file):
            for num in state:
                file = file.lower()
                if re.search(regex % num, file):
                    print(num)
                    splittedName = re.split(regex % num, file)
                    link = os.path.abspath(file)
                    renameFile(num, link, states, splittedName)
                    break

def getCurrentStates(state: States):
    srcMap = {"": state.none,
              "@hovered": state.hovered,
              "@pressed": state.pressed,
              "@disabled":state.disabled}

    dstMap = {}
    count: int = 1
    for key in srcMap.keys():
        if srcMap.get(key) == True:
            dstMap["_0" + str(count)] = key
            count +=1
    return dstMap

def renameFile(numb: str, link: str, map: {}, splittedName:[]):
    for index in splittedName:
        if index == "_" + numb + ".":
            count = splittedName.index(index)
            splittedName[count] = map.get("_" + numb) + "."
            os.rename(link, os.getcwd() + '\\' + str.join("", splittedName))


get = lambda **kwargs: type('', (object,), dict(**kwargs))()
"""
test: States = States()
test.none = True
test.hovered = True
test.pressed = True
test.disabled = True
"""
renameFiles(link, get(none=True, hovered=True, pressed=True, disabled=True))


