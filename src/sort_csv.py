import csv
import os
from datetime import datetime

#use multiprocessing to sort large csv file in disk
'''
ToDo: implement below methods to handle csv files

'''


class CsvException(Exception):
    pass

class CsvHandler:

    def __init__(self):
        '''init method'''
        self.sort_dir = '.csvsorter.{}'.format(datetime.now())
        os.makedirs(self.sort_dir , exist_ok=True)
        self.max_memory_size = 40 

    def read_csv(self, input_filename):
        '''read csv file and craete reader object'''
        with open(input_filename, 'r', encoding='utf-8') as input_fp:
            reader = csv.reader(input_fp, delimiter=',')
            header = next(reader)
            #splitting csv files into chunks
            self.split_csv(reader)            

    def split_csv(self, reader):
        '''split csv into multiple csvs'''
        self.max_memory_size  = self.max_memory_size  * 1024 * 1024 # convert to bytes
        current_size = 0
        file_count = 1
        fout = None
        filename = os.path.join(self.sort_dir, 'part{}.csv'.format(file_count))
        fout = open(filename, 'w', newline='\n', encoding='utf-8')
        writer = csv.writer(fout)

        # break CSV file into smaller merge files
        for row in reader:
            writer.writerow(row)
            current_size += sys.getsizeof(row)
            if current_size > self.max_memory_size :
                writer = None
                fout.close()
                file_count +=1
                filename = os.path.join(self.sort_dir, 'part{}.csv'.format(file_count))
                fout = open(filename, 'w', newline='\n', encoding='utf-8')
                writer = csv.writer(fout)
                current_size = 0

        if not fout.closed:
          fout.close()

    def sort_csv(self):
        '''sort csv'''

    def merge_csv(self):
        '''merge csv'''
