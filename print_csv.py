import csv
# a function for printing csv files
def print_csv(filename):
    with open(filename, 'r') as read_file:
        reader = csv.reader(read_file)
        for row in reader:
            print(row)
