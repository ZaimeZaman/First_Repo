#Q.4: Write a program in Python to input a single character and print a message
#"it is a vowel" if it vowel otherwise print message "It is a constant".
#use match-case structure and oR(||) operator only...

print("\n\n\t***This is a Vowel identifier program***\n\n")
a=input("Enter a single word :")

print("\n\t<<<Output>>>\n")
print(f" 1. '{a}' you entered.")
match a:
    case 'a':
        print(f" 2. This '{a}' is an Vowel.")
    case 'e':
        print(f" 2. This '{a}' is an Vowel.")
    case 'i':
        print(f" 2. This '{a}' is an Vowel.")
    case 'o':
        print(f" 2. This '{a}' is an Vowel.")
    case 'u':
        print(f" 2. This '{a}' is an Vowel.")
    case 'A':
        print(f" 2. This '{a}' is an Vowel.")
    case 'E':
        print(f" 2. This '{a}' is an Vowel.")
    case 'I':
        print(f" 2. This '{a}' is an Vowel.")
    case 'O':
        print(f" 2. This '{a}' is an Vowel.")
    case 'U':
        print(f" 2. This '{a}' is an Vowel.")
    case _:
        print(f" 2. This '{a}' is a constant.")
print("\n\t***THANKS***\n\n")