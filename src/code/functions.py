'''
Created on 22 Jul 2014

@author: Colin
'''


def functionName():
    ''' This is a function '''
    pass

def add(x,y):
    ''' This is a function '''
    return x + y

def printMessage():
    print('This function prints this message')


# This is equivalent to the Java main method
if __name__ == '__main__':
    
    print(add(1,2))
    
    printMessage()