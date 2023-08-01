#Q.2: Write a program in Python t input four integers.
#find out the largest value and then it on the screen by using 
#nested if structure...

print("\n\n\t***This is the program to find the largest value***\n\n")
a=int(input("Enter the 1st value :"))
b=int(input("Enter the 2nd value :"))
c=int(input("Enter the 3rd value :"))
d=int(input("Enter the 4th value :"))

print("\n\t<<<Output>>>\n\n")
if a>b:
    if a>c:
        if a>d:
            print(f"#. The 1st={a} value is largest then all.")
    else:
        print("")
if b>a:
    if b>c:
        if b>d:
            print(f"#. The 2nd={b} value is largest then all.")
    else:
        print("")
if c>a:
    if c>b:
        if c>d:
            print(f"#. The 3rd={c} value is largest then all.")
    else:
        print("")
if d>a:
    if d>b:
        if d>c:
            print(f"#. The 4th={d} value is largest then all.")
    else:
        print("")
    
print("\n\t***THANKS***\n\n")