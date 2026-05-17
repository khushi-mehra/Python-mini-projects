marks1 = int(input("enter first number:"))
marks2 = int(input("enter second number:"))
marks3 = int(input("enter third number:"))

total_marks = marks1 + marks2 + marks3 

percentage = (total_marks / 300)* 100 

if percentage >= 90 :
    grade = "A"

elif percentage >= 80 :
    grade = "B"

elif percentage >= 70 :
    grade = "C"

else :
    grade = "fail"

print("total_marks =", total_marks)
print("percentage =", percentage)
print("grade =", grade)

