# Python program to display all the prime numbers within an interval

lower = 1
upper = 100

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

           # Multiplication table (from 1 to 10) in Python

           num = 12

           # To take input from the user
           # num = int(input("Display multiplication table of? "))

           # Iterate 10 times from i = 1 to 10
           for i in range(1, 11):
               print(num, 'x', i, '=', num * i)

for number in range(100,0,-1):
    print(number)
