# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 09:40:25 2019

@author: leann
"""

# RUNNING A TEST TO GIVE A CLEAR ERROR MESSAGE

try:
    f = open('testfile')
except Exception:
    print('Error!')
    
    PRINTS OUT:
    Error!
    
try:
    f = open('testfile')
except Exception:
    print('Sorry, this file appears nto to exist, or the file name is wrong. \n\nPlease double check')
    
   PRINTS OUT:
   Sorry, this file appears nto to exist, or the file name is wrong. 

Please double check
   
   
   # DEALING WITH MULTIPLE ERRORS
   
try:
    f = open('testfile.txt')
    s1 = not_exists
except Exception:
    print('Sorry this file appears not to exist or the file  name is incorrect.  \n\nPlease double check')
    
    #PRINTS OUT:
    Sorry this file appears not to exist or the file  name is incorrect.  

Please double check
    
        
try:
    f = open('testfile.txt')
    s1 = not_exists
except FileNotFoundError:
    print('Sorry this file appears not to exist or the file  name is incorrect.  \n\nPlease double check')
    
    #PRINTS OUT:
    Sorry this file appears not to exist or the file  name is incorrect.  

Please double check
    
    
    #  TASK 1
    
try:
    f = open('testfile.txt')
    s1 = not_exists
except Exception as e:
    print(e)
    
    # PRINTS OUT:
    
    [Errno 2] No such file or directory: 'testfile.txt'
    
    
    #  TASK 2
try: 
    f = open('testfile.txt')
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
    
    # PRINTS OUT:
    [Errno 2] No such file or directory: 'testfile.txt'
    
    
    #   TASK 3
try:
    f = open('testfile')
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print('Execuing finally.....')
    
    
    
    #------
    # MANUALLY RAISING AN EXCEPTION
    #------
    
try:
    f = open('testfile.txt')
    if f.name == 'testfile.txt':
        raise Exception
except Exception as e:
        print('File names are the same')
    
    
        
    