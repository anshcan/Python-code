# dict = {1 : 2 , 3 : 4 , 5 : 6}
# print (dict[3])

# dict["city"]="Indore" #add
# print(dict)

# dict[1]=5 #update
# print(dict)

# dict.update({"city:":"indore"})
# print(dict)

# print(dict.keys())
# print(dict.values())
# print(dict.items())
# print(dict.pop(1))
# print(dict.popitem())
# print(dict.get(3))
# dictnew=dict.copy()
# print(dictnew)
# dict.clear()
# print(dict)
# del dict
# print(dict)

#Dynamic dictionary 

# student={}
# print(type(dict))
# print(dict)
# n= int(input("Enter the limit : "))
# for i in range(0,n):
#     key=input("Enter the key : ")
#     data= input("Enter the value : ")
#     student.update({key:data})

# print(student)

# Nesed Dictionary 

student={
    1:{"id":1,"name":"abc"},
    2:{"id":2,"name":"mno"},
    3:{"id":3,"name":"xyz"}
}
print(student)
print(student[1]["id"])
print(student[2]["name"])
print(student[3]["id"])
