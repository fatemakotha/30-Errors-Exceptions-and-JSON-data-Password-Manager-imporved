import json

#THIS PAGE OF CODE IS NOT VALID, IT IS MERELY A SUGGESTION

# #Write
# json.dump()
#
# #Read
# json.load()
#
# #Update
# json.update()

with open("data.json","w") as data_file:  #write mode
    # opens in append mode and creates the file names info.txt as there is no file of that name here
    json.dump(data to enter, location to enter data in, indentation space number) ******
    json.dump(new_data, data_file, indent=4) #puts the new_data into the data_file

with open("data.json", "r") as data_file: #read mode
    data = json.load(data_file)
    print(data) #converts the JSON data and prints it as a dictionary