# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 09:27:27 2019

@author: leann
"""

#-----
# CHAPTER 2 - validation
#-----

#  CASTING to an INT

#age = int(input("Please let us know your age: "))
#print(age)



#-----
# VALIDATING STRING CONTENT - own content
#-----

#postage = input("Would you like your item posted?\n\n Please type yes or no:")
#
#print(input("You have declared {}.".format(postage)).UPPER())
#
#if len(userInput) == 2:
#    print('correct input')
#elif userInput == < 0:
#    print('Incorrect input')
    

#-------
# TEXT BOOK TASK
#-------


print('***Please choose an option.....***')
print('1. Display my name')
print('2. Display my age')
print('1. Display my location')

choice = int(input('What choice do you choose?:  '))

if choice == 1:
    print('Mr Jones')
    
elif choice == 2:
    print('28 years old')
    
elif choice == 3:
    print('Chester')
    


while choice < 1 or choice > 3:
    choice = int(input('What is your choice? '))
    
choice = 0

#-------
# HANDLING ERRORFUL INPUTS
#-------
