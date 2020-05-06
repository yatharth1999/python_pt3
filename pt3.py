#Theoretical Questions:
#1. What is the syntax to call a constructor of a base class from child class
#---By using Super keyword
#---super()._init_()
#
#2. How is a class made as inherited class (syntax of child class)
#---class child(parent)
#
#3. Print an element of a nested dictionary
dict = {1: {'Name': 'yatharth', 'age': '20'}, 2: {'Name': 'eioda', 'age': '38',}}
print(dict[1])
#Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
for i in range(1000 , 3001):
    j = str(i)
    if int(j[0])%2==0 and int(j[1])%2==0 and int(j[2])%2==0 and int(j[3])%2==0 :
        print(j)
#Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.
def sum(a, b):
    s = int(a) + int(b)
    return s
a=str(input("enter a no"))
b=str(input("enter a no"))
print(sum(a,b))