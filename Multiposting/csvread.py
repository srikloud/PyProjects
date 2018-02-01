# This script reads a GPS track in CSV format and
#  prints a list of coordinate pairs
import csv

output_file=open('C:/Users/C5259095/Downloads/Multiposting/sobey_output22.csv', 'w')
# Set up input and output variables for the script
gpsTrack = open("C:/Users/C5259095/Downloads/Multiposting/Sobeys_JobReqDetails.csv", "r")

# Set up CSV reader and process the header
csvReader = csv.reader(gpsTrack)
#header = csvReader.next
#latIndex = header.index("lat")
#lonIndex = header.index("long")

# Make an empty list
coordList = []

# Loop through the lines in the file and get each coordinate
for row in csvReader:
    print(row[:38] + row[40:], file=output_file)

output_file2=open('C:/Users/C5259095/Downloads/Multiposting/sobey_final_output2.csv', 'w')
gpsTrack_output = open("C:/Users/C5259095/Downloads/Multiposting/sobey_output2.csv", "r")
csvReader2 = csv.reader(gpsTrack_output)

file = open("C:/Users/C5259095/Downloads/Multiposting/sobey_output2.csv", "r")
contents = file.read()
replaced_contents = contents.replace('[', '')
final_contents = replaced_contents.replace(']', '')

print(final_contents, file=output_file2)

'''
for row in csvReader2:
    str2 = str(row)
    #str1 = str(row).replace('[','')
    #str2 = str1.replace(']','')
    print(str2, file=output_file2)
'''



