Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 13:49:07) [MSC v.1938 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def add(a,b):
    return a+b
def subtract (a,b ):
    return a-b
def multipy(a,b):
    return a*b 
def divide (a,b):
    if b==0:
        print("can't divide by zero")
        return 0
...     else:
...         return a/b
...     while True :
...         print ("\n select operation:")
...         print ("q.Quit")
...         print("1.Add")
...         print("2.Subtract")
...         print("3.Multiply")
...         print("4.Divide")
...         
...         choice = input("Enter choice:")
...         choice == 'q':
...             break
...             if choice in['1','2','3','4']:
...                 num1= float (input("Enter first number:"))
...                 num2= float (input("Enter second number:"))
...                 
...                 if choice== '1':
...                     result = add (num1,num2)
...                  print ("the result is:", result)  
...                 
...                 elif choice== '2':
...                     result = subtract (num1,num2)
...                  print ("the result is:", result)  
...                 
...                 elif choice== '3':
...                     result = multiply (num1,num2)
...                  print ("the result is:", result) 
...                 
...                 elif choice== '4':
...                     result = divide (num1,num2)
...                  print ("the result is:",result)  
...                 
...                 else :
...                     print ("Invalid input")
...                 
...                 
>>> [DEBUG ON]
>>> [DEBUG OFF]
