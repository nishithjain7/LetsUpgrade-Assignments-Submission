#Assignment Day_2

#Q1. Name the keyword which helps in writing code involving conditions.
#Ans. If, elif and Else are three keywords involved in writing conditional statements. 
#Q2. Write the syntax of a simple if statement.
#Ans. If (expression):
          #(statement)
     #else:
         #(statement)


#Q3. Write a program to check whether a person is eligible for voting or not. (accept age from user)
age = int(input("Enter age of Person:"))
if age >= 18:
    print("Person Is Eligible to Vote")
else:
    print("Person is Not Eligible to Vote!! But can encourage others")


#Q4. What is the output of the given below program?

if 1 + 3 == 7:
    print("Hello")
else:
    print("Know Program")
Ans Know Program
 
#Q5. Write a program to check whether a number entered by user is even or odd.
num1=int(input("Enter Number to check:"))
if num1%2==0:
    print("The Number is Even")
else:
    print("The Number is Odd")


#Q6. Python program to find the largest element among three Numbers ?

num1 = 10 
num2 = 50 
num3 = 15
a=10
b=50
c=15
if a>b and a>c:
    print("Maximum number is",a)
elif b>a and b>c:
    print("Maximum number is",b)
else:
    print("Maximum number is",c)

#07. Write a program to accept a number from 1 to 12 and display name of the month and days in that month like 1 for January and number of days 31 and so on
month_num=int(input("Enter Month Number:"))

if month_num == 2:
	print("Feburary No. of days: 28/29 days")
elif month_num == 1:
	print("January No. of days: 31 days")
elif month_num == 3:
	print("March No. of days: 31 days")
elif month_name == 4:
	print("April No. of days: 30 day")
elif month_num == 5:
	print("May No. of days: 31 days")
elif month_name == 6:
	print("June No. of days: 30 day")
elif month_num == 7:
	print("July No. of days: 31 days")
elif month_name == 8:
	print("August No. of days: 31 day")
elif month_name == 9:
	print("September No. of days: 30 day")
elif month_name == 10:
	print("October No. of days: 31 day")
elif month_name == 11:
	print("November No. of days: 30 day")
elif month_name == 12:
	print("December No. of days: 31 day")
else:
	print("Wrong month Number Enter between 1 to 12")

