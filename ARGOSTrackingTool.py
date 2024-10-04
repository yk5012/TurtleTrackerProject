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
 
#Ask user for a date 
user_date = '7/3/2003' #input("Enter a date(mm/dd/yyyy): ")

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

#Initialize empty list for keys
keys = []

#Loop through items in date_dict to see if it matches input list 

    #For each item in the date_dict that i am calling 'item', the key is the first thing and value is the second thing
    #(we took a look and saw that each item is (unique id, date)
    #if value == user_date, print that key 
    #So this prints all unique ids for a specified user_date 

for item in date_dict.items(): #date_dict.items() pulls up all items(key and value pairs) in date_dict
    key = item[0]
    value = item[1]
    if value == user_date:
        keys.append(key) #append selected key to the empty 'keys' list we created

    #Since this is a tupule we can also do:
    #for key, value in date_dict.items():
        #if value == user_date:
            #print(key)

#Loop through keys and report location 
for key in keys:
    location = location_dict[key]
    lat = location[0]
    long = location[1]
    print(f"On the date {user_date}, Sara the turtle was seen at {lat}d lat, {long}d long.")




