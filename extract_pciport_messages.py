import os
import re
import sys

def main():
    fileName = ""
    #Get Filename from paramaters
    try:
        if sys.argv.__len__() > 0:
            fileName = sys.argv[1]
        if not (os.path.isfile(fileName)):
            raise FileNotFoundError("File path {} does not exist. Enter valid filepath...".format(fileName))
    except Exception:
        print("File path {} does not exist. Give valid file path as parameter .(eg: testFile.txt )".format(fileName))
        sys.exit(0)
    extractPciPort(fileName)

def extractPciPort(fileName):
    with open(fileName + "_pciport_messages.txt", "a") as outputFile:
        with open(fileName) as file:
            currentLine = file.readline()







if __name__ == '__main__':
    main()