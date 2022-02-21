import csv
def mock_data():
#creating mock csv files for data input and testing
 with open('CUSTOMERS.csv', 'w', newline='') as file1:
    writer = csv.writer(file1)
    writer.writerow(["CUSTOMER_CODE", "FIRSTNAME", "LASTNAME"])
    writer.writerow(["CUST0000010231", "Maria", "Alba"])
    writer.writerow(["CUST0000010235","George", "Lucas"])
    writer.writerow(["CUST0000010240","Rick", "Morty"])

 with open('CUSTOMER_SAMPLE.csv', 'w', newline='') as file_sample:
    writer = csv.writer(file_sample)
    writer.writerow(["CUSTOMER_CODE"])
    writer.writerow(["CUST0000010231"])
    writer.writerow(["CUST0000010235"])

 row_list = [["CUSTOMER_CODE", "INVOICE_CODE", "AMOUNT", "DATE"],
             ["CUST0000010231","IN0000001","105.50","01-Jan-2016"],
             ["CUST0000010235","IN0000002","186.53","01-Jan-2016"],
             ["CUST0000010231","IN0000003","114.14","01-Feb-2016"],
             ["CUST0000010240","IN0000004","113.12","14-Feb-2022"]]
 with open('INVOICES.csv', 'w', newline='') as file2:
    writer = csv.writer(file2)
    writer.writerows(row_list)

 row_list = [["INVOICE_CODE", "ITEM_CODE", "AMOUNT", "QUANTITY"],
            ["IN0000001","MEIJI","75.60","100"],
            ["IN0000001","POCKY","10.40","250"],
            ["IN0000001","PUCCHO","19.50","40"],
            ["IN0000002","MEIJI","113.40","150"],
            ["IN0000002","PUCCHO","73.13","150"],
            ["IN0000003","POCKY","16.64","400"],
            ["IN0000003","PUCCHO","97.50","200"],
            ["IN0000004","MEIJI","100.00","100"]]
 with open('INVOICE_ITEM.csv', 'w', newline='') as file3:
    writer = csv.writer(file3)
    writer.writerows(row_list)