Name = input("Name: ")
Age = int(input("Age: "))
Gpa = float(input("Enter your GPA btw (0-5): "))
Graduated = input("Are you graduated?: ")
Field = input("Enter your field of interest: ")
print("Name :" +Name)
print("Age :" +str(Age))
print("Gpa:" +str(Gpa))
print ("your interest:" +Field)
print("Graduated : " +Graduated)
is_grad = Graduated == "yes"
scholarship  = Age < 25 and Gpa >=3.5 and is_grad
internship = Age < 30 and Gpa >= 2.5 
if scholarship:
   
    print("You are eligible for a scholarship")
elif internship:
    print("You are eligible for an internship")
else:
    print("please apply again")
