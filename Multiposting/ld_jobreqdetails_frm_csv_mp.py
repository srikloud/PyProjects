import csv
import os
import pyhdb
import re

connection = pyhdb.connect(host="ld9345.wdf.sap.corp", port=34215, user="SYSTEM", password="manager")
cursor = connection.cursor()


def lod_jobreqdets():
    output_file = open('C:/Users/C5259095/Downloads/Multiposting/MP_OUTPUT/output_JobReqDetails.csv', 'w', encoding="utf-8")
    error_file = open('C:/Users/C5259095/Downloads/Multiposting/MP_OUTPUT/error_JobReqDetails.csv', 'w', encoding="utf-8")
    #directory_in_str = "C:/Users/C5259095/Downloads/Multiposting/temp3/5year/SRSD_15327_DC4pool1/SRSD_15327_DC4pool1"
    directory_in_str = "C:/Users/C5259095/Downloads/Multiposting/5year_JobDesc_Merge/Pool1"

    directory = os.fsencode(directory_in_str)

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        #print(filename)
        if (filename.lower().endswith("jobreqdetails.csv")) and ('test' not in filename.lower()) and ('perf' not in filename.lower()):
            print(filename)
            str1 = os.path.join(directory_in_str, filename)
            formatfile = (str1.replace("\\", "/"))
            inputfile = open(formatfile,"r",encoding='utf-8', errors='ignore')
            csvReader = csv.reader(inputfile)

            cnt = 0
            firstline = True
            for row in csvReader:
                if firstline:
                    firstline = False
                    continue
                else:
                    try:
                        line = str(row[:38] + row[40:]).replace('[', '').replace(']', '')
                        line1 = re.sub('\"[^"]*\"', lambda x:x.group(0).replace("'","").replace(",",""),line)
                        line2 = line1.replace('"',"'")
                        #print(line2, file=output_file)
                        query_string = 'INSERT INTO WORKFORCE.SF_RAW_JOBREQDETAILS VALUES(%s)' %line2
                        cursor.execute(query_string)
                        cnt = cnt +1
                        if cnt == 1000:
                            print("1k records commited")
                            connection.commit()
                            cnt = 0
                    except:
                        print(filename, file=error_file)
                        print(line2, file=error_file)
                        pass
                connection.commit()
                continue
            else:
                continue
    connection.commit()
    cursor.close()

'''

cursor = connection.cursor()
query_string = 'INSERT INTO WORKFORCE.SF_RAW_JOBREQDETAILS VALUES (%s);' % line
cursor.execute(query_string, line)
connection.commit()
cursor.close()
'''



'''
output_file2=open('C:/Users/C5259095/Downloads/Multiposting/sobey_final_output2.csv', 'w')
gpsTrack_output = open("C:/Users/C5259095/Downloads/Multiposting/sobey_output2.csv", "r")
csvReader2 = csv.reader(gpsTrack_output)

file = open("C:/Users/C5259095/Downloads/Multiposting/sobey_output2.csv", "r")
contents = file.read()
replaced_contents = contents.replace('[', '')
final_contents = replaced_contents.replace(']', '')

print(final_contents, file=output_file2)
'''


lod_jobreqdets()

