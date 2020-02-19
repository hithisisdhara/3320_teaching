# DO NOT DELETE EXISTING CODE LINES unless told to do so in the comments
def int_to_word(i):
    word = ""
    #######################
    # Fill your code here, use as many new lines you like. Delete this line.
    # you will get a zero if this method doesn't return a string
    #######################
    return word
    
print "Enter an integer from 1 to 99:"
s = raw_input()
try:
    a = int(s)
    if a < 1 or a > 99:
        print("This method only works for integers from 1 to 99")
    else:
	word = int_to_word(a)
        print("The given number in words:")
        print(word)
except:
    print("Method only works for integers")
    
#--------------------------------------------------------------
'''
Expected outcome:

>> python q6.py
Enter an integer from 1 to 99:
>> 10
"The given number in words:
Ten
>> 

>> python q6.py
Enter an integer from 1 to 99:
>> 101
This method only works for integers from 1 to 99
>>

>> python q6.py
Enter an integer from 1 to 99:
>> yaw
Method only works for integers
>>

'''
