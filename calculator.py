
#Main function
def main():
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    
    choice = input("Choose Operation: \n 1 - Addition \n 2 - Subtraction \n 3 - Division \n 4 - Multiplication \n").lower()
    
    if choice == '1' or choice == 'addition':
        print(addition(x, y))
    elif choice == '2' or choice == 'subtraction':
        print(subtraction(x, y))
    elif choice == '3' or choice == 'division':
        print(division(x, y))
    elif choice == '4' or choice == 'multiplication':
        print(multiplication(x, y))
    else:
        print("Error")

#Operations        
def addition(m, n):
    return m + n

def subtraction(m, n):
    return m - n

def division(m, n):
    return m / n

def multiplication(m, n):
    return m * n
    
    
main()