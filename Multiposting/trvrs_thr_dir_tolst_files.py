import os
from pathlib import Path


def trvs_dir():
    directory_in_str = "C:/Users/C5259095/Downloads/Multiposting/temp3/5year/SRSD_15327_DC4pool2/SRSD_15327_DC4pool2"


    directory = os.fsencode(directory_in_str)
    print(directory)
    for file in os.listdir(directory):
        #print(file)
        filename = os.fsdecode(file)
        #print(filename)
        if filename.endswith("_JobReqDetails.csv") or filename.endswith(".py"):
            #str1 = filename.replace("\\", "/")
            str1 = os.path.join(directory_in_str, filename)
            print(str1.replace("\\", "/"))

            continue
        else:
            continue


'''
    pathlist = Path(directory_in_str).glob('**/*.asm')
    print(pathlist)
    for path in pathlist:
        print('hello')
        # because path is object not string
        path_in_str = str(path)
        print(path_in_str)
'''

trvs_dir()