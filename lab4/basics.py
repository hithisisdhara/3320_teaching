print "hi there" # doesn't work in python 3 
print("hi there")
string = "hi there"  # doesn't work in python 3
print(string)
print string

a = 5
b = 10
if b % a == 0:
    print str(b) + " is divisible by " + str(a)
else:
    print "no can dooz"

try:
    print(string + a)
except:
    print("I tried printing an int with string :(")
    print("I got error")

try:
    print(a)
    print("I can print an integer by itself without casting it into string")
except:
    print("no lucks :( ")


to_print = ""
for i in range(5):
    to_print += str(i) + " "
print("output of range(5)")
print(to_print)

to_print = ""
for i in range(1, 5):
    to_print += str(i) + " "
print("output of range(1,5)")
print(to_print)

to_print = ""
for i in range(5, -1, -1):
    to_print += str(i) + " "
print("output of range(5, -1, -1)")
print(to_print)



d = {
    1: "one",
    2: "two",
    3: "three"
}
print("dictionary access:")
print(d[1])
try:
    print d[10]
except:
    "I tried getting d[10]. \n 10 is not a key in the dictionary "
    print(d)

string = "Please input an integer"
print(string)
s = raw_input()
try:
    a = int(s)
    print("Thank you for listening to me!")
except:
    print ("I told you,"+string)

