#%% Task 4.1 - Reading in the data and displaying the column headers

#Create a Python file object, i.e., a link to the file's contents
fileObj = open(file='data/raw/transshipment_vessels_20180723.csv',mode='r')

#Read the entire contents into a list object
lineList = fileObj.readlines()

#Release the link to the file objects (now that we have all its contents)
fileObj.close() #Close the file

#Save the contents of the first line in the list of lines to the variable "headerLineString"
headerLineString = lineList[0]

#Print the contents of the headerLine
print(headerLineString)


#%% Task 4.2 - Splitting the header string into a list of column names and extracting index values

#Split the headerLineString into a list of header items
headerItems = headerLineString.split(',')

#List the index of the mmsi, shipname, and fleet_name values
mmsi_idx = headerItems.index('mmsi')
name_idx = headerItems.index('shipname')
fleet_idx = headerItems.index('fleet_name')

#Print the values
print(mmsi_idx,name_idx,fleet_idx)


#%% Task 4.3 - Iterating through the data lines and adding values to a dictionary
#Create an empty dictionary
vesselDict = {}
#Iterate through all lines (except the header) in the data file:
for lines in lineList[1:]:
    #Split the data into values
    vesselData = lines.split(',')
    #Extract the mmsi value from the list using the mmsi_idx value
    mmsi = vesselData[mmsi_idx]
    #Extract the fleet value
    fleet = vesselData[fleet_idx]
    #Adds info to the vesselDict dictionary
    vesselDict[mmsi] = fleet


# %% Task 4.4 - Using the dictionary
#Assigning string value to vesselID
vesselID = '440196000'

#Using vesselID to lookup fleet value
fleetValue = vesselDict[vesselID]

#Printing statement using fleet value and vesselID
print(f'Vessel # {vesselID} flies the flag of {fleetValue}')


# %% Task 5
#Create a Python file object, i.e., a link to the file's contents
fileObj = open(file='data/raw/loitering_events_20180723.csv',mode='r')

#Read the entire contents into a list object
loiteringList = fileObj.readlines()

#Release the link to the file objects (now that we have all its contents)
fileObj.close() #Close the file

#Save the contents of the first line in the list of lines to the variable "loiteringHeaderLineString"
loiteringHeaderLineString = loiteringList[0]

#Split the loiteringHeaderLineString into a list of header items
loiteringHeaderItems = loiteringHeaderLineString.split(',')

#List the index of the transshipmentmmsi, starting latitude, ending latitude, starting longitude and ending longitude values
transshipmentmmsi_idx = loiteringHeaderItems.index('transshipment_mmsi')
startLat_idx = loiteringHeaderItems.index('starting_latitude')
endLat_idx = loiteringHeaderItems.index('ending_latitude')
startLong_idx = loiteringHeaderItems.index('starting_longitude')
endLong_idx = loiteringHeaderItems.index('ending_longitude')

#Creating boolean variables for latitude, longitude, and noVessels criteria
latCondition = False; longCondition = False; vesselsCriteriaMet = False

#Iterate through all lines (except the header) in the data file:
for lines in loiteringList[1:]:
    #Split the data into values
    loiteringData = lines.split(',')

    #Extract the transshipment_mmsi value from the list using the transshipmentmmsi_idx value
    transshipmentmmsi = loiteringData[transshipmentmmsi_idx]
    
    #Extract the latitude and longitude values and storing them as float values 
    startLat = float(loiteringData[startLat_idx])
    endLat = float(loiteringData[endLat_idx])
    startLong = float(loiteringData[startLong_idx])
    endLong = float(loiteringData[endLong_idx])
  
    #Evaluating cross-equator criteria
    if((startLat < 0) and (endLat > 0)): 
        latCondition = True #Set latitude boolean variable to true if criteria is met

        #Evaluating starting longitude criteria
        if((startLong > 145) and (startLong < 155)):
            longCondition = True #Set longitude boolean variable to true if criteria is met

        else:
            longCondition = False #Set longitude boolean variable to false if criteria is not met
    
    else:
        latCondition = False #Set latitude boolean variable to false if criteria is not met
        

    if(latCondition and longCondition):
        vesselsCriteriaMet = True #Set vesselsCriteriaMet boolean variable to true if both criteria are met at least once
        
        #Extract fleet value using transshipmentmmsi and print statement 
        fleetValue = vesselDict[transshipmentmmsi]
        print(f'Vessel #{transshipmentmmsi} flies the flag of {fleetValue}')
    else:
        continue

#Printing statement if no vessels meet criteria
if (vesselsCriteriaMet == False):
    print('No vessels met criteria')

# %%
