#Python Loops

#while loop
mySampleIntValue=68
while(mySampleIntValue<=80):
    print("Desired number is: "+str(mySampleIntValue))
    mySampleIntValue+=1
print("**********************************************************")

#for loop
mySampleString="Every day is a beautiful day."
for letter in mySampleString:
    print(letter,end="")
print("")
print("**********************************************************")

#for loop with range
for number in range(1,20,2):
    print("Number is: "+str(number))
print("**********************************************************")

#for loop with else
for number in range(6):
    print(number)
else:
    print("The for loop with else is finally finished.")
print("**********************************************************")

#Nested for loops
color_list=['red','green','yellow']
fruit_list=['apple','banana','mango']
for x in fruit_list:
    for y in color_list:
        print(x+" is having color: "+y)
print("**********************************************************")