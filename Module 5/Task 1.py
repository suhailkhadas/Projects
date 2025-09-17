try:
    students_dictt={"Alice":"70","Jhon":"80"}
    student_name=str(input("Enter the Student's name: "))
    print(student_name+"'s marks: "+students_dictt[student_name])
except:
    print("{}  not Found".format(student_name))