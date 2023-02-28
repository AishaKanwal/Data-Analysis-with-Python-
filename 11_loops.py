#while loops and for loops

#while loops
# x=0
# while (x<=5):
#     print(x)
#     x=x+1 #to make the loop finite 

#for loop
# for x in range(4,10):
#     print(x)

#array 
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
for d in days:
    # if (d=="friday"):break #loop stops till thursday
    if (d=="friday"):continue #skips only friday 
    print(d)