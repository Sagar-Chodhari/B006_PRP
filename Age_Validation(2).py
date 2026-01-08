def teenager():
    print("Teenager") 
    
def adult():
    print("Adult")
    
def senior_citizen():
    print("Senior Citizen")
    
    
age = int(input("Enter your age: "))

if age < 18:
    teenager()

elif age > 18 and age < 50:
    adult()
        
else :
    senior_citizen()
        
