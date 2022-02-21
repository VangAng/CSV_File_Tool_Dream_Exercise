import csv
#creating the extracted output csv file
def Create_Extracted_File( filename, entries):
        with open(filename, 'w', newline='') as file:
          writer = csv.writer(file)
          for row in entries:
            writer.writerow(row)
        return filename
        