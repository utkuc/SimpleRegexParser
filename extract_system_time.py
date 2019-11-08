import os
import re
import sys


def main():
    fileName = ""
    try:
        if sys.argv.__len__() > 0:
            fileName = sys.argv[1]
        if not (os.path.isfile(fileName)):
            raise FileNotFoundError("File path {} does not exist. Enter valid filepath...".format(fileName))
    except Exception:
        print("File path {} does not exist. Give valid file path as parameter .(eg: testFile.txt )".format(fileName))
        sys.exit(0)
    extractSystemTime(fileName)


def extractSystemTime(fileName):
    with open(fileName) as file:
        currentLine = file.readline()
        linecounter = 0
        while currentLine:
            print("currentLine {}: {}".format(linecounter, currentLine.strip()))
            currentLine = file.readline()
            linecounter += 1

if __name__ == '__main__':
    main()
