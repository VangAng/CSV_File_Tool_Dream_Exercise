import csv
# a function for searching and retrieving data from a csv file according to particular keys/codes
def Search_Retrieve(file_name,codes,entries):
  #open the csv file for retrieving the data
  with open(file_name, 'r') as input_file:
           reader = csv.reader(input_file)
           #get the length of the codes list in order to use it as iterator
           ran=list(range(len(codes)))
           for row in reader:
             for i in ran:
               # searching for a matching entry
               if row[0]==codes[i]:
                 #retrieve matching entries and put them in a list
                entries.append(row)
           return entries 