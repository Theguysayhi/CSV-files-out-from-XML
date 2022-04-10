import sys
import xml.etree.ElementTree as ET
class xmlManager:

    def extractCSVdata(self, filename):
        output = []
        mytree = ET.parse(filename)
        myroot = mytree.getroot()
        #Iterate through the XML in case there are multiple transactions.
        for transaction in myroot.findall('./Transactions/Transaction'):
            text = transaction.find('./MeterDataNotification/CSVIntervalData').text.strip()
            #Check formatting is correct, data leads with 100 and ends with 900
            if (text[0:3]=='100') and (text[-3:]=='900'):
                output.append(text)
            else:
                print("Encountered an error in the CSV, is it formatted correctly?", file=sys.stderr)
                output.append("CSV FORMAT ERROR")
        return(output)

    def getCSVData(self, filename, index=0): #default index is 0 assming there is only one group of data
        return(self.extractCSVdata(filename)[index])


XMLhelper = xmlManager()
data = XMLhelper.getCSVData('Testfiles/testfile.xml')
with open('output.csv', 'w') as f:
    f.write(data)




