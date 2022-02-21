from file_tool_final import file_process
from print_csv import print_csv
from get_codes import get_codes
from input_data import mock_data

#create mock input csv file
mock_data()
files_IN=['CUSTOMERS.csv', 'INVOICES.csv','INVOICE_ITEM.csv']
files_OUT=['CUSTOMERS_EXTRACTED.csv','INVOICES_EXTRACTED.csv','INVOICE_ITEM__EXTRACTED.csv']
sample_file='CUSTOMER_SAMPLE.csv'

#producing 1st extracted file
keys=get_codes(sample_file,"CUSTOMER_CODE")
file_process(files_IN[0], files_OUT[0],keys)

#producing 2nd extracted file
file_process(files_IN[1], files_OUT[1],keys)

#producing 3rd extracted file
keys=get_codes('INVOICES_EXTRACTED.csv', "INVOICE_CODE")
file_process(files_IN[2], files_OUT[2],keys)

#printing the final output files
for name in files_OUT:
    print_csv(name)
    print()