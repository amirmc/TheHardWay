# Exercise 13 (extra credit): Parameters, Unpacking, Variables

from sys import argv

script, age_arg, height_arg, weight_arg = argv

print "The script is called:", script

bKnowBMI = raw_input("Do you want to know your BMI? (y/n): ")

if bKnowBMI == 'y':
    print "Your BMI is:", eval(weight_arg)/(eval(height_arg)**2)
elif bKnowBMI == 'n':
    print "Stop being such a wuss"
else:
    print "Need to choose either 'y' or 'n'"

print "End of script called %s" % script