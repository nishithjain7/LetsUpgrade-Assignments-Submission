#Q1. Python program to print Highest Common Factor (HCF) of two numbers
#Example : Take values according to you
num1 = int(input("Enter first Number:"))
num2 = int(input("Enter Second Number:"))
if num1>num2:
    smaller_num = num1
else:
    smaller_num = num2
for i in range(1,smaller_num+1):
    if ((num1%i==0)and(num2%i==0)):
        hcf = i

print("The H.C.F. of",num1,"and",num2,"is",hcf)

#Q2. What will be the output of the following Python code?
i=0
def change(i):
    i=i+1
    return i
change(1)
print(i)
#a) 1
#b) Nothing is displayed
#c) 0
#d) An exception is thrown
#Ans. c)0

#Q3. What will be the output of the following Python code?
def a(b):
    b = b + [5]
c = [1, 2, 3, 4]
a(c)
print(len(c))
#Ans. 4

#Q4. What will be the output of the following Python code?
a=10
b=20
def change():
    global b
    a=45
    b=56
change()
print(a)
print(b)
#a)
#10
#56
#b)
#45
#56
#c)
#10
#20
#d) Syntax Error
#Ans #a)
     #10
     #56

#Q5. What will be the output of the following Python code?
def change(i = 1, j = 2):
    i = i + j
    j = j + 1
    print(i, j)
change(j = 1, i = 2)
#a) An exception is thrown because of conflicting values
#b) 1 2
#c) 3 3
#d) 3 2
#Ans. d) 3 2
