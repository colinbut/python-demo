'''
Created on 22 Jul 2014

@author: Colin
'''

'''This example demonstrates classes in Python'''

class Person(object):
    '''
    classdocs
    '''
    
    forename = ''
    surname = ''
    age = 0
    dateOfBirth = ''

    def __init__(self, f, s, a, dob):
        '''
        Constructor
        '''
        self.forename = f
        self.surname = s
        self.age = a
        self.dateOfBirth = dob
    
    def displayName(self):
        '''
        Prints the persons name (both first and surname) on screen
        '''
        print(self.forename , self.surname)
        
        
        
        