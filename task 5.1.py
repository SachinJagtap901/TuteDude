stud_name =input("Enter Student Name : ")
a = {'sachin':98,'Ravi':77,'Tejas':88}
try:
    marks = a[stud_name]
    print(f"{stud_name}'s marks :  {a[stud_name]}")
except KeyError:
    print("Student Not Found")