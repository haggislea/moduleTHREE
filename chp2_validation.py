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

#print("Would you like your item posted?\n\n Please type yes or no:")
#
#postageRequired = input()
#
#while True:
#    if len(postageRequired) == 3:
#        print(("You have declared {}.".format(postageRequired)))
#    
#else:   
#        print('This is invalid.\n\n It is a Yes or No answer, thank you.')
        
       

#-------
# TEXT BOOK TASK
#-------


#print('***Please choose an option.....***')
#print('1. Display my name')
#print('2. Display my age')
#print('3. Display my location')
#
#choice = input('What choice do you choose?:  ')
#
#if choice == 1:
#    print('Mr Jones')
#    
#elif choice == 2:
#    print('28 years old')
#    
#elif choice == 3:
#    print('Chester')
#    
#  
#choice = 0
#
##-------
## HANDLING ERRORFUL INPUTS
##-------

print('***Please choose an option.....***')
print('1. Display my name')
print('2. Display my age')
print('3. Display my location')

choice = input('What choice do you choose?:  ')

while True: 
    try:
        if choice == 1:
            print('Mr Jones')
    
        elif choice == 2:
            print('28 years old')
    
        elif choice == 3:
            print('Chester')
        
        while choice < 1 or choice >3:
            choice = int(input('What is your choice?'))
            break
        
    except ValueError:
        print('Type a number!')
        
        
#class Spam(object):
#    def __init__(self, description, value):
#        if not description or value <=0:
#            raise ValueError
#        self.description = description
#        self.value = value
#            
#s = Spam('s', 5)
#print('s', 5)

