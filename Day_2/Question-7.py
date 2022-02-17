#07. Write a program to accept a number from 1 to 12 and display name of the month and days in that month like 1 for January and number of days 31 and so on
month_num=int(input("Enter Month Number:"))

if month_num == 2:
	print("Feburary No. of days: 28/29 days")
elif month_num == 1:
	print("January No. of days: 31 days")
elif month_num == 3:
	print("March No. of days: 31 days")
elif month_num == 4:
	print("April No. of days: 30 day")
elif month_num == 5:
	print("May No. of days: 31 days")
elif month_num == 6:
	print("June No. of days: 30 day")
elif month_num == 7:
	print("July No. of days: 31 days")
elif month_num == 8:
	print("August No. of days: 31 day")
elif month_num == 9:
	print("September No. of days: 30 day")
elif month_num == 10:
	print("October No. of days: 31 day")
elif month_num == 11:
	print("November No. of days: 30 day")
elif month_num == 12:
	print("December No. of days: 31 day")
else:
	print("Wrong month Number Enter between 1 to 12")

