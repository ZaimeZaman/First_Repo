#Q.4: Write a program in Python to input a single character and print a message
#"it is a vowel" if it vowel otherwise print message "It is a constant".
#use if-else structure and oR(||) operator only...

print("\n\n\t***This is a vowel indentifier program***\n\n")

a=input("Enter any single word :")

print("\n\t<<<Output>>>\n")
print(f" 1. You have enter '{a}' word.")
if (a=='a' or a=='e' or a=='i' or a=='o' or a=='u'):
    print(f" 2. The '{a}' is an vowel.")
elif(a=='A' or a=='E' or a=='I' or a=='O' or a=='U'):
    print(f" 2. The '{a}' is an vowel.")
else:
    print(f" 2. The '{a}' is a constant.")
    print("\tPlease try again...")

print("\n\t***THANKS***\n\n")