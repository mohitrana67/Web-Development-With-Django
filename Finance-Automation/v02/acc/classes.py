import csv, io

class ReadCSV():
    def __init__(self,data_set):
        self.data_set = data_set

    def read_csv(self):
        result = []
        io_string = io.StringIO(self.data_set)
        # next(io_string)
        for column in csv.reader(io_string, delimiter=','):
            temp_arr = []
            for i in range(len(column)):
                temp_arr.append(column[i])
            result.append(temp_arr)
        
        return result