import pyhdb

def con_to_saphana():
    connection = pyhdb.connect(host="ld9345.wdf.sap.corp", port=34215, user="SYSTEM", password="manager")
    cursor = connection.cursor()

    tabcount = cursor.execute("SELECT COUNT(*)FROM WORKFORCE.SF_RAW_JOBREQDETAILS")
    #connection.commit()
    print(tabcount.fetchall())

    tabtrunc = cursor.execute("TRUNCATE TABLE WORKFORCE.SF_RAW_JOBREQDETAILS")
    print(tabtrunc)

    tabcount2 = cursor.execute("SELECT COUNT(*)FROM WORKFORCE.SF_RAW_JOBREQDETAILS")
    #connection.commit()
    print(tabcount2.fetchall())

    cursor.close()


    connection.close()

'''
    cursor2 = connection.cursor()
    val = cursor2.execute("SELECT * FROM ETL.CONCUR_TEST_LOAD")

    data = val.fetchall()
    for i in data:
        print(i)

    cursor2.close()

    cursor3 = connection.cursor()
    cursor3.execute("INSERT INTO ETL.CONCUR_TEST_LOAD(FIELD1) VALUES(400)")
    connection.commit()
    print(cursor3.rowcount)
    cursor3.close()

    cursor4 = connection.cursor()
    val = cursor4.execute("SELECT * FROM ETL.CONCUR_TEST_LOAD")

    data = val.fetchall()
    for i in data:
        print(i)

    cursor4.close()

'''




con_to_saphana()