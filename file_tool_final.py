# the main file tool that processes the files
# from the input csv file it produces the extracted output file based on the pre-selected keys
from Search_Retrieve import Search_Retrieve
from Create_Extracted_File import Create_Extracted_File

def file_process(filename_in,filename_out, keys):
    entries=[]
    entry1=Search_Retrieve(filename_in,keys,entries)
    Create_Extracted_File(filename_out, entry1)
