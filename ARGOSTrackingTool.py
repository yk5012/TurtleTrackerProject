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
file_object = open(file_name,'r')

#Read contents of file into a list
line_list = file_object.readlines()

#Close the file since we have a list with whole file now
file_object.close()

#Initialize empty dictionaries using {}
date_dict = {}
location_dict = {}

#Pretend we read one line of data from the file
for lineString in line_list: # instead of using if, can also do line_list[17:] to read only from line 18
    #Check if line is a data line
    if lineString[0] in ("#", "u"): # if start of line(index 0) has # or u, skip 
        continue 
   
    #Split the string into a list of data items
    lineData = lineString.split()

    #Extract items in list into variables
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_lon = lineData[7] 

    #Determine if location criterion is met
    #If observation class is either 1, 2, or 3, will add to dictionaries. 
    #no.s need to be string not int bc they are read in string 
    if obs_lc in ("1", "2", "3"): #else: skip. 
        #Add items to dictionary 
        date_dict[record_id] = obs_date #adding each line's unique record id to dict
        location_dict[record_id] = (obs_lat, obs_lon)

    #Print the location of sara
   # print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")

