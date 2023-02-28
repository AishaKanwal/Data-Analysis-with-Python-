x=10            #int
y=10.2          #float  
z="Hello!"      #string

#implicit type conversion 
# x=x*y           #changing int to float 

# print(x, "type of x is: ",type(x))
# print(type(y))
# print(type(z))

#explicit type conversion
age=input("What is your age? ")
# age=int(age)            
print(age, type(float(age)))

#name
name=input("what is your good name? ")
print(name, type(str(name)))
