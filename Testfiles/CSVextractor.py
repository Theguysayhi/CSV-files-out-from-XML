import xml.etree.ElementTree as ET


class xmlManager:

    def getCSVdata(filename):
        mytree = ET.parse(filename)
        myroot = mytree.getroot()
        print(myroot)

    def outputCSV(filename):
        getCSVdata(filename):


        return

xmlManager.extractCSV('testfile.xml')




