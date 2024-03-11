"""
Sesiunea 15 - Exercitii cu Trainer
"""
import csv
import json

"""
1. 
a. Creeaza un fisier csv, numit 'students.csv' cu 
urmatorul continut:

id,fname,lname,age,grade
1,Maria,Popescu,31,7.5
2,Andrei,Ionescu,26,8.0
3,Adriana,Marinescu,21,7.5
4,Matei,Gheorghescu,42,8.5
5,Eusebiu,Pop,33,9.5
6,Ioana,Popa,29,9.0

b. Citeste continutul fisierului csv si afiseaza informatiile
din acesta in consola, ca un tabel, folosind optiunile
de formatare string-uri:

id	fname		lname		age	grade
---------------------------------------------------
1	Maria		Popescu		31	7.5
2	Andrei		Ionescu		26	8.0
3	Adriana		Marinescu		21	7.5
4	Matei		Gheorghescu	42	8.5
5	Eusebiu		Pop			33	9.5
6	Ioana		Popa			29	9.0
"""

# with open('students.csv', 'w') as file:
#     writer = csv.writer(file)
#
#     writer.writerow(['id', 'fname',  'lname','age', 'grade'])
#     writer.writerow([1, 'Maria', 'Popescu', 31, 7.5])
#     writer.writerow([2, 'Andrei', 'Ionescu', 26, 8.0])
#     writer.writerow([3, 'Adriana', 'Marinescu', 21, 7.5])
#     writer.writerow([4, 'Matei', 'Gheorghescu', 42, 8.5])
#     writer.writerow([5, 'Eusebiu', 'Pop', 33, 9.5])
#     writer.writerow([6, 'Ioana', 'Popa', 29, 9.0])

students_list = []

with open('students.csv', 'r') as file:
    # reader = csv.reader(file)
    lines = file.readlines()
    print(f"id\tfname\t\tlname\t\tage\tgrade\n{50*'-'}")

    for row in lines[1:]:
        # dispatch - luam fiecare elem din colectie si il punem intr-o variabila
        id, fname, lname, age, grade = row.strip().split(',')
        # print(f"{id}\t{fname}\t\t{lname}\t\t{age}\t{grade}")

        student = {
		    "id": id,
		    "fname": fname,
		    "lname": lname,
		    "age": age,
		    "grade": grade
	    }

        students_list.append(student)
# print(students_list)

with open('students.json', 'w') as file:
    json.dump(students_list, file)

"""
2. Citeste din nou continutul fisierului csv, salveaza continutul
sau intr-o lista si apoi creeaza un nou fisier, 'students.json',
in care sa ai aceleasi informatii (intr-un format JSON valid) 

Foloseste urmatorul format pentru fiecare student:

[
	{
		"id": 1,
		"fname": "Maria",
		"lname": "Popescu",
		"age": 31,
		"grade": 7.5	
	},
	...
]
"""




"""
3. 
a. Creeaza o clasa Student, pe baza datelor din exercitiul de mai sus. 
b. Citeste fisierul JSON creat si pune datele intr-o lista cu obiecte Student
b. Adauga inca cateva obiecte Student in lista si scrie noul continut intr-un
nou fisier JSON.
"""


class Student:
    def __init__(self, id, fname, lname, age, grade):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.age = age
        self.grade = grade


student = Student(1, "Andrei", 'Laiu', 25, 10)
student2 = Student(2, "Maria", "Pop", 12, 9)
student3 = Student(3, "Ion", "Ionescu", 20, 5)

list2 = []
list2.extend([student, student2, student3])


with open('studenti.json', 'w') as file:
    json.dump(list2, file)

