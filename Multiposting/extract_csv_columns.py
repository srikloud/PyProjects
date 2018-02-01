import re
import sys, argparse, csv


def extract_csv_cols():


    f = open('C:/Users/C5259095/Downloads/Multiposting/test_file.csv', "r", encoding='utf-8', errors='ignore')

    print(f)


    with open('C:/Users/C5259095/Downloads/Multiposting/test_file.csv','rb') as csvfile:
        # get number of columns
        for line in csvfile.readlines():
            print(line)
            #array = line.split(',')

        '''
        for line in csvfile.readlines():
            array = line.split(',')
            first_item = array[0]

        num_columns = len(array)
        csvfile.seek(0)

        reader = csv.reader(csvfile, delimiter=' ')
        included_cols = [1, 2, 6, 7]

        for row in reader:
            content = list(row[i] for i in included_cols)
            print(content)

'''

extract_csv_cols()
