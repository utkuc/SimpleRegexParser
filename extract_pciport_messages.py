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
#Extract pci port with relative time and description
def extractPciPort(fileName):
    with open(fileName + "_pciport_messages.txt", "a") as outputFile:
        with open(fileName) as file:
            currentLine = file.readline()
            while currentLine:
                pciport = re.search("([0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F]:)"
                                    "([0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F]"
                                    ":"
                                    "[0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F]"
                                    "[.]"
                                    "[0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F]|"
                                    "[0-9a-fA-F][0-9a-fA-F]:[0-9a-fA-F][0-9a-fA-F][.][0-9a-fA-F])", currentLine)
                if pciport:
                    date = re.search(r"\b(0[  0-9]|1[0-9]|2[0-4])(:)([0-5][0-9])(:)[0-5][0-9]\b", currentLine)
                    if date:
                        description = re.search("(?<=kernel:\s).*$", currentLine)
                        if description:
                            outputFile.write(str(date[0]).replace(" ", "") + "\t")
                            outputFile.write(str(pciport[0]) + "\t")
                            outputFile.write(str(description[0]) + "\n")
                currentLine = file.readline()


if __name__ == '__main__':
    main()