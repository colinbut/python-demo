'''
Created on 22 Jul 2014

@author: Colin
'''

if __name__ == '__main__':
    
    
    try:
        a = 0
        b = 2
        
        sum = b / a
        print(sum)
    
    except ZeroDivisionError:
       # pass
       print('Cannot divide by zero!')
    except:
        print('Catching all other types of errors')
        #
    finally:
        pass
        