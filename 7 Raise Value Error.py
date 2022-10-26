


height = float(input("HEIGHT: "))
weight = float(input("WEIGHT: "))

#Human height is less than 3 meters
if height > 3: #if height inputted is 45
    raise ValueError("Human height should not be over 3 meters") #which says the the value entered is wrong and
                                                                 #displays the message "Human height should not be over 3 meters"
bmi = weight / height ** 2
print(bmi)

#PRINTS:
# HEIGHT: 55
# WEIGHT: 2
# Traceback (most recent call last):
#   File "C:\Users\fatem\PycharmProjects\fatemakotha\30-Errors-Exceptions-and-JSON-data-Password-Manager-imporved\main.py", line 9, in <module>
#     raise ValueError("Human height should not be over 3 meters") #which says the the value entered is wrong and
# ValueError: Human height should not be over 3 meters