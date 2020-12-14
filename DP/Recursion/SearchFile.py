import os
from os.path import isfile, join


print(join("C:\\dev", "readme.txt"))

def search(fullFilePath, filename):
    print("checking: " + fullFilePath)

    ## stopping condition
    if filename in fullFilePath:
        print("Found " + filename + " in " + fullFilePath)
        return
    # if file not directory
    if isfile(fullFilePath):
        return

    for file in os.listdir(fullFilePath):
        search(join((fullFilePath, file), filename))

def searchAndQuitIfFound(fullFilePath, filename):
    print("checking: " + fullFilePath)

    ## stopping condition
    if filename in fullFilePath:
        print("Found " + filename + " in " + fullFilePath)
        return True

    # if file not directory
    if isfile(fullFilePath):
        return False

    for file in os.listdir(fullFilePath):
        found = search(join((fullFilePath, file), filename))
        if found: return True

    return False

search("C:\\tools", "test.sh")

## 1. step: if found then stop search
## 2. step: do not stop after finding file


search("C:\\tools", "test.sh")

## 1. step: if found then stop search
## 2. step: do not stop after finding file


