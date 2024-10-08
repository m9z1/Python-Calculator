#Importing Modules
import math


#Main function
def main():
    choice = input("Choose Operation: \n 1 - Addition \n 2 - Subtraction \n 3 - Division \n 4 - Multiplication \n 5 - Exponents \n 6 - Square Root \n").lower()
    
    if choice == '1' or choice == 'addition':
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        print(addition(x, y))
    elif choice == '2' or choice == 'subtraction':
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        print(subtraction(x, y))
    elif choice == '3' or choice == 'division':
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        print(division(x, y))
    elif choice == '4' or choice == 'multiplication':
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        print(multiplication(x, y))
    elif choice == '5' or choice == 'exponents':
        x = float(input('Enter a number: '))
        y = int(input('Enter the power: '))
        print(exponents(x, y))
    
    elif choice == '6' or choice == 'square root':
        x = int(input("Enter the number: "))
        print(sqroot(x))
        
    else:
        print("Error")

#Operations        
def addition(m, n):
    return m + n

def subtraction(m, n):
    return m - n

def division(m, n):
    if n == 0:
        return 'Error!! Cannot divide by zero'
    return m / n

def multiplication(m, n):
    return m * n
    
def exponents(m, n):
    return m ** n    

def sqroot(m):
    return math.sqrt(m)
    
main()