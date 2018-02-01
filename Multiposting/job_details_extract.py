import csv
import os
import pyhdb
import re




def lod_jobreqdets():
    output_file = open('C:/Users/C5259095/Downloads/Multiposting/MP_OUTPUT/output_OfferDetJobAppExt_pool1.csv', 'w', encoding="utf-8")
    error_file = open('C:/Users/C5259095/Downloads/Multiposting/MP_OUTPUT/error_JobReqDetails.csv', 'w', encoding="utf-8")
    #directory_in_str = "C:/Users/C5259095/Downloads/Multiposting/temp3/5year/SRSD_15327_DC4pool1/SRSD_15327_DC4pool1"
    #directory_in_str = "C:/Users/C5259095/Downloads/Multiposting/6YearMerge/SRSD_15327_DC4pool1/SRSD_15327_DC4pool1"
    directory_in_str = "C:/Users/C5259095/Downloads/Multiposting/6YearMerge/SRSD_15327_DC4pool1/SRSD_15327_DC4pool1"
    #directory_in_str = "C:/Users/C5259095/Downloads/Multiposting"

    directory = os.fsencode(directory_in_str)

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        #print(filename)
        if (filename.endswith("Prologis_OfferDetJobAppExt.csv")) and ('test' not in filename.lower()) and ('perf' not in filename.lower()):
        #if (filename.lower().endswith("sobeys_jobreqdetails.csv")) and ('test' not in filename.lower()) and ('perf' not in filename.lower()):
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
                        for i in range(0, len(row)):
                            row[i] = row[i][:2000]
                        #print(row)
                        #row[0] = row[0][:3]
                        #print(row[0])
                        #line = str(row[:38] + row[40:]).replace('[', '').replace(']', '')
                        line = str(row).replace('[', '').replace(']', '')
                        print(line)
                        #line0 = re.sub('\"[^"]*\"', lambda x:x.group(0).replace("'",""),line)
                        #line00 = re.sub('\"[^"]*\"', lambda x:x.group(0).replace(",", ""), line0)
                        #line1 = line00.replace("'",'')
                        print(line, file=output_file)
                    except:
                        print(filename, file=error_file)
                        print(line, file=error_file)
                        pass

                continue
            else:
                continue


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

