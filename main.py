#lists
student = ["Fatima", 10, 5, "China"]
print(student)

#add
student.append("My hobby is skating")
print(student)

#length
print("numbers of items in the lists", len(student))

a = [3,4,4,5,3,3,4,9,8]
print("maximum number in the list", max(a))
print("minimum number in the list", min(a))
(a.sort())
print(a)
a.reverse()
print(a)
print("first value in the list", a[0])
print("third value in the list", a[3])
print(a[6:9])
a.insert(9,5)
print(a)
print(a.index(8))
a.remove(3)
print(a)