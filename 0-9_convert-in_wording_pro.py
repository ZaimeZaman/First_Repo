#Q.5: Write a program in python to input a single digit
#from 0 to 9 and print the input value in words.
#For example if the input value is 0. then print "zero"
#use the switch statement...

print("\n\n\t***This is a Number to word convert of 0-9***\n\n")
a=int(input("Enter the number between 0-9 :"))

print("\n\t<<<Output>>>\n\n")
print(f" 1. {a} you entered.")
match a:
    case 0:
        print(f" 2. {a} : 'Zero'.")
    case 1:
        print(f" 2. {a} : 'One'.")
    case 2:
        print(f" 2. {a} : 'Two'.")
    case 3:
        print(f" 2. {a} : 'Three'.")
    case 4:
        print(f" 2. {a} : 'Four'.")
    case 5:
        print(f" 2. {a} : 'Five'.")
    case 6:
        print(f" 2. {a} : 'Six'.")
    case 7:
        print(f" 2. {a} : 'Seven'.")
    case 8:
        print(f" 2. {a} : 'Eight'.")
    case 9:
        print(f" 2. {a} : 'Nine'.")
    case _:
        print(f" 2. {a} is not between 0-9.")
        print("Please try again...")
print("\n\t***THANKS***\n\n")