import csv
import os
import pyhdb
import re
import itertools
import datetime
import sys

connection = pyhdb.connect(host="ld9345.wdf.sap.corp", port=34215, user="SYSTEM", password="manager")
cursor = connection.cursor()
cursor.fast_executemany = True


def lod_jobreqdets():
    output_file = open('C:/Users/C5259095/Downloads/Multiposting/MP_OUTPUT/output_JobReqDetails.csv', 'w', encoding="utf-8")
    error_file = open('C:/Users/C5259095/Downloads/Multiposting/MP_OUTPUT/error_JobReqDetails.csv', 'w', encoding="utf-8")
    #directory_in_str = "C:/Users/C5259095/Downloads/Multiposting/temp3/5year/SRSD_15327_DC4pool1/SRSD_15327_DC4pool1"
    directory_in_str = "C:/Users/C5259095/Downloads/Multiposting/5year_JobDesc_Merge/Pool1"

    directory = os.fsencode(directory_in_str)

    print("&&&&&&&&&&&   Load Started  &&&&&&&&&&")
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        #print(filename)
        if (filename.lower().endswith("cerrejon_jobreqdetails.csv")) and ('test' not in filename.lower()) and ('perf' not in filename.lower()):
            print(filename)
            str1 = os.path.join(directory_in_str, filename)
            formatfile = (str1.replace("\\", "/"))
            inputfile = open(formatfile,"r",encoding='utf-8', errors='ignore')
            csvReader = csv.reader(inputfile)


            a = []
            a1 = []
            i = 0
            k = 0
            cnt = 0
            cnt1 =0
            firstline = True

            print("#######   Load Started for file :"+ str(filename))
            query_string = "INSERT INTO WORKFORCE.SF_RAW_JOBREQDETAILS(JOB_REQ_ID,	TEMPLATE_ID,	JOB_REQ_TITLE,	JOB_CODE,	JOBREQ_START_DATE,	JOBREQ_END_DATE,	CUSTOM_STATUS,	INTERNAL_STATUS,	JOB_DEPARTMENT,	JOB_DIVISION,	JOB_LOCATION,	LAST_MODIFIED,	JOB_START_DATE,	DAILY_OPP_COST,	COST_OF_HIRE,	JOB_LEVEL,	JOB_TYPE,	JOB_GRADE,	SALARY_MAX,	SALARY_MID,	SALARY_MIN,	SAL_ACCEPTED,	COMMISSION,	COMMISSION_PACK,	OPTIONS,	OPTIONS_PACK,	OTHER_BONUS,	OTHER_COMPENSATION,	CURRENCY,	RELOCATION_COST,	RELOCATION_PACK,	SIGNON_BONUS,	STOCK,	STOCK_PACKAGE,	NONRECOVERABLE_DRAW,	RECOVERABLE_DRAW,	EEO_ESTABLISHMENT,	EEO_GROUP,	CANDIDATE_HIRED,	DATE_CREATED,	INTRANET_POSTING,	CORPORATE_POSTING,	ACTUAL_START_DATE,	CANDIDATE_PROGRESS,	FORM_DATA_ID,	CLASSIFICATION_TYPE,	CLASSIFICATION_TIME,	JOB_FUNCTION,	INDUSTRY,	LAST_MODIFIED_BY,	CITY,	STATE_PROVINCE,	POSTALCODE,	COUNTRY,	FILTER1,	FILTER2,	FILTER3,	FILTER4,	FILTER5,	FILTER6,	FILTER7,	FILTER8,	FILTER9,	FILTER10,	FILTER11,	FILTER12,	FILTER13,	FILTER14,	FILTER15,	OVERALL_SCALE_NAME,	ASSESS_RATING_SCALE_NAME,	REVERSE_SCALE,	RCM_APP_STATUS_SET_ID,	SALARY_BASE,	SAL_RATE_TYPE,	OVERTIME_RATE,	TARGET_BONUS_PERCENT,	TARGET_BONUS_AMOUNT,	BONUS_PAYOUT_FREQ,	NUMBER_OPENING,	OPENING_FILLED,	DEFAULT_LOCALE,	TEMPLATE_TYPE,	DATE_CLOSED,	JOB_REQ_GUID,	APPLICATION_TEMPLATE_ID,	RATED_APPLICANT_COUNT,	PACKAGE_ID,	COSTCENTER_ID,	ONBOARDING_PACKAGE_ID,	BGI_ACCOUNT_ID,	COMPANY_VISIBILITY,	LAST_MODIFIED_PROXY_USERID,	FACILITY,	REQUIRED_TRAVEL,	BRAND,	ERP_AMOUNT,	HARDSTOP_STATUS_ID,	JOB_ROLE,	TIME_TO_FILL,	AGE,	POSITION_NUMBER,	IS_DELETED,	LEGAL_ENTITY_OBJ,	BUSINESS_UNIT_OBJ,	DEPARTMENT_OBJ,	DIVISION_OBJ,	COST_CENTER_OBJ,	LOCATION_OBJ) values(%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s)"
            print("***************  Load Started  ************  :"+ str(datetime.datetime.now()))
            for row in csvReader:
                for i in range(0, len(row)):
                    row[i] = row[i][:2000]
                a.append(row[:38] + row[40:])
                cnt1 = cnt1 +1
                if firstline:
                    firstline = False
                    continue
                else:
                #print(row)
                    cnt = cnt + 1
                    if cnt == 250:
                        try:
                            print("count "+str(cnt))
                            cnt = 0
                            print("*******  500 Records Exec Started************  :" + str(datetime.datetime.now()))
                            number_of_rows = cursor.executemany(query_string, a)
                            #connection.commit()
                            print("*******  500 Records Exec Ended************  :" + str(datetime.datetime.now()))
                            print("number_of_rows " + str(number_of_rows))
                            a = []
                            number_of_rows = 0
                        except:
                            print("Error in the File "+filename, file= error_file)
                            #connection.commit()
                            pass

                continue
            try:
                print("*******  Rest of Records Exec Started************  :" + str(datetime.datetime.now()))
                number_of_rows = cursor.executemany(query_string, a)
                connection.commit()
                print("*******  Rest of Records Exec Ended************  :" + str(datetime.datetime.now()))
                print("number_of_rows " + str(number_of_rows))
                a = []
                number_of_rows =0
                print("#######  Load Completed for file :" + str(filename))
            except:
                print("Error in last records in file: "+filename,file=error_file)
                connection.commit()
                a=[]
                pass

        continue
    print(cnt1)
    connection.commit()
    a=[]
    print("&&&&&&&&&&&  Load Ended   &&&&&&&&&&")
    cursor.close()
    connection.close()
    print("&&&&&&&&&&&  Cursor and Connection Closed   &&&&&&&&&&")



lod_jobreqdets()

