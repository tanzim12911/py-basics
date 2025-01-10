# Typecasting = the process of converting a variable from one data type to another
#               str(), int(), float(), bool()

name = "Bro Code"
age = 25
gpa = 3.2
is_student = True

print(type(name)) # using type func, we can find data type of a variable

gpa = int(gpa)
print(gpa)

age = str(age)
age += "1"
print(age)

name = bool(name)
name_2 = bool("")
print(name)
print(name_2)