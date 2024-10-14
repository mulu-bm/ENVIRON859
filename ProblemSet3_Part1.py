#%% Task 1 - Edit code to print as requested
#/*-PS3: Code Block 1--*/

mountain = "Denali"
nickname = 'Mt. McKinley'
elevation = 20322 

print (f'{mountain}, sometimes \ncalled \"{nickname}\",')
print (f'is {elevation}\' above sea level.')


#%% Task 2 - Lists and Iteration
#/*-PS3: Code Block 2--*/

#Assigning string and list variables
data_folder = "W:\\859_data\\triangle"
data_list = ["streams.shp", "stream_types.csv", "naip_imagery.tif"]
user_item = "roads.shp"

#Adding the user_item variable to the list
data_list.append(user_item)

#Looping through list and printing file paths
for item in data_list:
    filepath = data_folder + "\\" + item
    print(filepath)


#%% Task 3 - Lists and Iteration
#/*-PS3: Code Block 3--*/

#Creating empty list
user_numbers = []

#Iterating 3 times to accept input numbers and add them to list
for i in range(3):
    number = int(input("Enter an integer:"))
    user_numbers.append(number)

#Sorting numbers in list in ascending order
user_numbers.sort()

#Extracting and printing highest value
highest_number = user_numbers[-1]
print(f"The highest numnber is {highest_number}")


#%% Task 3 - Challenge
#/*-PS3: Task 3 Challenge--*/

#Creating empty list
user_numbers = []

#Iterating 3 times to accept input numbers and add them to list
for i in range(3):
    number = int(input("Enter an integer:"))
    user_numbers.append(number)

#Sorting numbers in list in descending order
user_numbers.sort(reverse=True)

#Printing entire contents of list
print(user_numbers)
# %%
