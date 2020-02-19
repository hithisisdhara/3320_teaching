# DO NOT DELETE EXISTING CODE LINES unless told to do so in the comments
# you will get a zero if 906609 is hardcoded 
def is_palendrome(a):
    #######################
    # Fill your code here, use as many new lines you like. Delete this line.
    # you will get a zero if this method doesn't return boolean 
    #######################
    return True  # you can delete/change this line and write new

max_pal = 0 
start = 0  # change the value of this variable
end = 0 # change the value of this variable 
for i in range(start, end):
    for j in range(i, end):
        product = i * j
        if is_palendrome(product):
            #######################
            # Fill your code here, use as many new lines you like. Delete this line.
            # make sure that max_pal indeed stores maximum value 
            #######################

print("The number you are looking for is:")
print max_pal
#--------------------------------------------------------------
'''
Expected outcome:
>> python q5.py
The number you are looking for is:
906609
>>
'''
