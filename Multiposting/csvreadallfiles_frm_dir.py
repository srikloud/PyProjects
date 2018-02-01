import csv

output_file=open('C:/Users/C5259095/Downloads/Multiposting/MP_OUTPUT/output_JobReqDetails.csv', 'w')

inputfile = "C:/Users/C5259095/Downloads/Multiposting/*_JobReqDetails.csv"
jobreqfile = open("C:/Users/C5259095/Downloads/Multiposting/Sobeys_JobReqDetails.csv", "r")

csvReader = csv.reader(jobreqfile)
coordList = []

for row in csvReader:
    #print(row[:38] + row[40:], file=output_file)
    print(str(row[:38] + row[40:]).replace('[', '').replace(']', ''))


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




