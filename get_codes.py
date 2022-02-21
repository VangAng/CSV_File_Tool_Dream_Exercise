import csv
# a function for getting the keys-codes from the csv file in order to access the other files
def get_codes(filename,key):
    codes=[]
    with open(filename, 'r') as input_file:
           #maps the information to a dictionary 
           #whose keys are given by the column names and all the values as keys
           reader = csv.DictReader(input_file)
           codes.append(key)
           for col in reader:
                codes.append(col[key])
           return codes