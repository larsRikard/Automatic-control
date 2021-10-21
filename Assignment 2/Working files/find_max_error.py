import csv
import numpy

def csvToArray(file, delimiter, transpose=False):
    """
    Reads a csv file
    :param file: string, name of file
    :param delimiter:
    :return:
    """
    try:
        with open(file, "r") as csvFile:
            reader = csv.reader(csvFile, delimiter=delimiter)
            for row in reader:
                x = list(reader)
                result = numpy.array(x)
            csvFile.close()
        if(transpose):
            return result.T
        return result
    except OSError as e:
        print(e)
        return None

def main():
    data = csvToArray("C:\Master\Automatic-control\Assignment 2\Working files\exportedVariables.csv", ",")
    max = float(data[0][1])
    max_index = 0
    for i in range(1,len(data)):
        if float(data[i][1]) > max:
            max = float(data[i][1])
            max_index = i
    print(f'{max = }, at time = {data[max_index][0]}')

if __name__ == "__main__":
    main()