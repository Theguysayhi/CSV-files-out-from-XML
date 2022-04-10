import xml.etree.ElementTree as ET


class xmlManager:

    def extractCSVdata(self, filename):
        output = []
        mytree = ET.parse(filename)
        myroot = mytree.getroot()
        #Iterate through the XML in case there are multiple transactions.
        for transaction in myroot.findall('./Transactions/Transaction'):
            output.append(transaction.find('./MeterDataNotification/CSVIntervalData').text)
        return(output)

    def getCSVData(self, filename, index):
        return(self.extractCSVdata(filename)[index])

XMLhelper = xmlManager()
print(XMLhelper.getCSVData('Testfiles/testfile.xml', 0))




