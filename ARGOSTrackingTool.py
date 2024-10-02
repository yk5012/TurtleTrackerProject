#-------------------------------------------------------------
# ARGOSTrackingTool.py -this is called front matter(similar to README)
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: John Fay (john.fay@duke.edu)
# Date:   Fall 2024
#--------------------------------------------------------------
 
#Create a variable pointing to the data file path relative to this file 
file_name = './data/raw/sara.txt' # . indicates start from current python file

#Create a file object from the file
file_object = open(file_name,'r') # we can't close this because need to go back to file for each line

#Read one line of file into a list 
#Smaller memory footprint than reading the whole file
lineString = file_object.readline()

#Pretend we read one line of data from the file
while lineString:    #This is a boolean that will be True if line has content, False if no content.
                        # Can also do while len(lineString) > 0: or 
    if lineString[0] in ("#", "u"): # if start of line(index 0) has # or u, skip 
        lineString = file_object.readline()  # need to read next line before 'continue' so it changes the line we are reading. if this line no exist lineString never changes
        continue 
   
    #Split the string into a list of data items
    lineData = lineString.split()

    #Extract items in list into variables
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_lon = lineData[7]

    #Print the location of sara
    print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")

    #Read next line 
    lineString = file_object.readline()

