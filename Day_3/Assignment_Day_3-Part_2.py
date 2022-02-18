#1. Run the following lines of code and explain the error in your own words. Then rewrite the lines of code to run error free:
#d = {one:1, two:2, three:3}
#d[one]
#Ans: This code was used to define dictionary. Its a rule that while defining string in python inverted comma are used but since they were not used it gave error
#In second line while getting form key also needs to be defined in inverted commas
#Correct Command
d = {'one':1, 'two':2, 'three':3}
d['one']

#2. Run the following lines of code and explain the error in your own words. Then rewrite the lines of code to run error free:
#f = false
#not f
#Ans  Its a rule that while defining string in python inverted comma are used but since they were not used it gave error
#Correct Command
f = "false"
not f

#3. 1. Run the following lines of code and explain the error in your own words. Then rewrite the lines of code to run error free:
lst = [1,3,5]
lst[3]
#Ans
#Correct Command
lst = [1,3,5]
print(lst[2])
#In place of 2, 0 or 1 can be used
