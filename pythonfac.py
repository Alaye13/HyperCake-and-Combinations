# Ifenna ekwenem
# Mr Reaser
number = int(input("Enter a numberber: "))  
n = number
r = number   
factorial = 1 
def factorial_function (n):
    if number < 0:    
        print(" Factorial does no apply for negatives")    
    elif number == 0:    
        print(" Factorial of 0 is 1")    
    else:    
        for i in range(1,number + 1):    
            factorial = factorial*i    
   print("The factorial of the number",number,"is",factorial)    
   

def combination_function (n, r):
    if 0 <= r <= n:
        combination = ((factorial(n)) /  factorial(n-r) * ((factorial(r)) ))
    else:
        print("Remember: 0 <= r <= n")
        0
    print("The combination of",n,r,"is",combination)   

def hypercake_function (n , k):
    sum = 0
    i = 0
    for x in range(i, k):
        sum = combination(n , r)
        hypercake_function = sum
    
       