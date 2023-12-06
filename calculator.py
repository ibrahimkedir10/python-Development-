num1= input("enter number")
num2 = input("enter second number")
result = int(num1)+ int(num2)
print(result)


## better way 
num1= int(input("enter number"))
num2 = int(input("enter second number"))
operator = input("enter operator")

def output():
    if operator == "+" :
        return num1 +num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 % num2
    else:
        return "invalid operator"
        
        
        
        
        
result = output() 
print(result)

