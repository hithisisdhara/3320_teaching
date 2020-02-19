from q6 import int_to_word
from q7 import word_to_int

print("enter a number in word")
s = raw_input()
first = word_to_int(s)
print("Enter another word in word")
s = raw_input()
second = word_to_int(s)

product = first * second
print("the multiplication is {}".format(product) )

#--------------------------------------------------------------
'''
Expected outcome:

>> python q8.py
enter a number in word
>> three
Enter another word in word
>> eleven
the multiplication is 33
>>
'''
