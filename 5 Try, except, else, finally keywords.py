# try: Something that might cause an exception
# except: Do this if there was an exception
# else: Do this if there were no exceptions
# finally: Do this no matter what happens

#tries a block of code:
try:
    file = open("a_file.txt") #the first time we run the code, the exception to this is carried out
    dictionary = {"key": "value"}
    print(dictionary["key"]) #the second time we run the code, the exception to this is carried out
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else: #when everything in the try block succeeds the block below is activated:
    content = file.read()
    print(content)
finally: #runs, no matter what happens
    file.close()
    print("File was closed")