import sys
import xml.etree.ElementTree as ET


class XmlManager:
    def csvbuilder(self, datalist):
        # build the csv string outputs
        csvlist = []
        cvno = 0
        datalist = datalist.split()
        firstline = datalist.pop(0)
        for line in range(len(datalist)-1):
            if datalist[line][0:3] == '200':  # add start of CV, first line at 100, second line at 200, and set name.
                if cvno > 0:
                    csvlist[cvno-1].append(csvlist[cvno-1].pop()+'900'+'\n')
                cvno += 1
                csvlist.append([datalist[line].split(',')[1], firstline+'\n'+datalist[line]+'\n'])
            elif datalist[line][0:3] == '300':  # add next line
                csvlist[cvno-1].append(csvlist[cvno-1].pop()+datalist[line]+'\n')
            elif datalist[line][0:3] == '900':
                print(datalist[line])
                print("End of data reached earlier than expected, make sure 900 only appears once.", file=sys.stderr)
                return csvlist
        csvlist[cvno-1].append(csvlist[cvno-1].pop()+'900')
        return csvlist

    def extractcsvdata(self, filename): # Returns the raw list of CSVs and their names
        mytree = ET.parse(filename)
        myroot = mytree.getroot()
        for transaction in myroot.findall('./Transactions/Transaction'):
            text = transaction.find('./MeterDataNotification/CSVIntervalData').text.strip()  # remove whitespace or tabs etc
            # Check formatting is correct, data leads with 100 and ends with 900
            if (text[0:3]!='100') or (text[-3:]!='900'):
                print("Encountered an error in the CSV, is it formatted correctly?", file=sys.stderr)
                return "CSV FORMAT ERROR"
        return self.csvbuilder(text)

    def tostring(self, filename, index=-1):  # returns the csv at the selected index, if needed
        data = self.extractcsvdata(filename)
        returnString = ''
        if index == -1:
            for x in range(len(data)):
                returnString += data[x][1]+'\n'
        else:
            returnString += data[index][1]
        return returnString.strip()

    def exporttocsvfromxml(self, filename):
        data = self.extractcsvdata(filename)
        for x in range(len(data)):
            with open(data[x][0]+'.csv', 'w') as f:
                f.write(data[x][1])
                f.close()


# --------------------------------------------------------
#print(XmlManager().tostring('Testfiles/testfile.xml'))
XmlManager().exporttocsvfromxml('Testfiles/testfile.xml')
print("Operation complete.")



