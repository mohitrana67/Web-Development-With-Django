import csv, io

class CSV:

    def __init__(self,file,uploadedFileTypeFlag):
        self.file = file
        self.flag = uploadedFileTypeFlag
    
    def read_csv_with_filelocation(self):
        sheet = []
        counter = 0
        if self.flag != 1:
            with open(self.file) as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                for row in readCSV:
                    if counter != 0:
                        temp_array = []
                        totalNoOfFields = len(row)
                        for i in range(0,totalNoOfFields):
                            temp_array.append(row[i])

                        sheet.append(temp_array)
                    counter += 1
        else:
            stream  = io.StringIO(self.file.stream.read().decode("UTF8"), newline=None)
            csv_input = csv.reader(stream)
            for row in csv_input:
                    if counter >= 0:
                        temp_array = []
                        totalNoOfFields = len(row)
                        for i in range(0,totalNoOfFields):
                            temp_array.append(row[i])
                    
                        sheet.append(temp_array)
                    counter += 1
            
        return sheet