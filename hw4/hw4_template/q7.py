# DO NOT DELETE EXISTING CODE LINES unless told to do so in the comments
def word_to_int(w):
    i = 0
    #######################
    # Fill your code here, use as many new lines you like. Delete this line.
    # you will get a zero if this method doesn't return an integer 
    #######################
    return i
    

f = open("num2word.txt")
count = 0
success = 0 
for line in f:
    count += 1
    line = line.replace("\n", "")
    gi = word_to_int(line)
    if (count != gi):
        print("issue", count, line)
        break
    else:
        success += 1 
f.close()
print ("all good for {} lines".format(success))
#--------------------------------------------------------------
'''
Expected outcome:

>> python q7.py
all good for 99 lines 
'''
