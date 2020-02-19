# DO NOT DELETE EXISTING CODE LINES unless told to do so in the comments


def is_leap_year(year):
    '''
    input: a year
    output: True if it is a leap year False otherwise 
    '''
    #######################
    # Fill your code here, use as many new lines you like. Delete this line.
    # keep the indent! 
    #######################
    return True # you can delete/change this line and write new 


if __name__ == "__main__":
    print("Please enter a year")
    s = raw_input()
    try:
        a = int(s)
        if is_leap_year(a):
            print("This is a leap year")
        else:
            print("this is not a leap year")
    except:
        print ("Not an integer")

#--------------------------------------------------------------
'''
Expected outcome:

>> python q3.py
Please enter a year
>> 2019
this is not a leap year
>>

>> python q3.py
Please enter a year
>> 2000
this is a leap year
>>

>> python q3.py
Please enter a year
>> 2500
This is not a leap year
>>
'''
