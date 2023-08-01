#Q.3: Write a program in python to input marks obtained by 
#student in a subject. The total marks are 100. find out 
#the grade of the student by using the if-else nested structure...

print("\n\n\t***This is a grade program***\n\n")

a=input("Enter the name of the subject :")
b=int(input(f"Enter your marks of {a} :"))
print("\n\n\t<<<Output>>>\n")
print(" 1. The subject name is :",a)
print(f" 2. The obtaining marks of {a} :{b}")
print(f" 3. The total marks of {a} subject : 100 ")
if b>90 :
    print(f" 4. The student got grade 'A+' in {a}")
elif b>70 :
    if b<90:
        print(f" 4. The student got grade 'A' in {a}")
elif b>50 :
    if b<70 :
        print(f" 4. The student got grade 'B' in {a}")
elif b<50:
    print(f" 4. The student got grade 'F' in {a}")
else:
    print("Please enter valid data...")

print("\n\t***THANKS***\n\n")