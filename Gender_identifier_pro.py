#Q.1: Write a program in python to input a single letter in a char variable.
#if "m" is input print "you are male" otherwise print "you are female" by using 
#conditional statement...

print("\n\n\t***This is the gender identifier***\n\n")
a=input("Enter your name :")
b=input("Enter your age :")
c=input("Enter your Gender by writting m/f :")

print("\n\n\t<<<Disply>>>\n\n")
print(" 1. Your name is :",a)
print(f" 2. You are {b} years old.")
if(c=='m'):
    print(" 3. You are a male.")
elif(c=='f'):
    print(" 3. You are a female.")
else:
    print(" 3. Kindly type m or f in small alphabates...")

print("\n\t***THANKS***\n\n")