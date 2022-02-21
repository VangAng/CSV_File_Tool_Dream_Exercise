# First, I created mock csv files for data input and testing.
# Function (get_codes) gets the pre-selected “keys” from the sample csv file in order to access the corresponding parts of the full csv files. 
# Then I “feed” these keys to the function Search_Retrieve in order to search, access and retrieve the parts from each full csv file. 
# Last, the Create_Extracted_File function writes the retrieved data to the new output file. 
# The file_tool_final function (using the previous two functions) is able to produce the desired output files given the corresponding input file.
