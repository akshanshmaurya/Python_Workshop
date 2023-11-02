my_dict ={}
student ={
    "Name":"akshansh",
    "Age":"24",
    "Grade":"A",
}
print(student)
student["Age"]=26
student["City"]="New York"
name=student["Name"]
Age=student["Age"]
print(student)
print(name)
print(Age)

for key in student.keys():
    print(f"{key}")

for values in student.values():
    print(f"{values}")

for key , value in student.items():
    print(f"{key}:{value}")


del student["Age"]
Age = student.get("Age")
print(Age)



dictionary={0:10,1:10}
dictionary[2]=30
print(dictionary)



dic1={0:10,1:20}
dic2={2:30,3:40}
dic3={4:50,5:60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)

