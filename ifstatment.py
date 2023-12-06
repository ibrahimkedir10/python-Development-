is_male = False
is_tall = False 

if(is_male):
    print("is male")
elif(is_tall):
    print("is tall")

else:print("all false statments")

# and or

if(is_male and is_tall):
    print("is male and tall")
elif(is_male and not is_tall):
    print("is male but short")
elif(is_male or is_tall):
    print("is one of them ")
    
  ## nums  
def nums(num1,num2,num3):
   
    if num1 == num2 and num2 == num3:
        return num1,num2,num3
    
    if num1 > num2  and num1>num3:
        return num1
    
    elif num3> num1 and num3> num2 :
        return num3
    else:
        return num2
result = nums(10,10,10)
print(result)
