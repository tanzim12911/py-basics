# Variable = A container for a value (string, integer, float, boolean)
#            A variable behaves as if it was the value it contains


# Strings
first_name = "Bro"
food = "pizza"
email = "Bro123@fake.com"

print(first_name)
print(f"Hello {first_name}")    # f-string
print(f"You like {food}")
print(f"Your email is {email}")

# Integers
age = 25
quantity = 3
num_of_students = 30

print(f"Your are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

# Float
price = 10.99
gpa = 3.2
distance = 5.5

print(f"The price is ${price}")
print(f"Your gpa is : {gpa}")
print(f"You ran {distance}km")

# Boolean (first letter capital)
is_student = True
for_sale = True

print(f"Are you a student?: {is_student}")

if for_sale:
    print("That item is for sale")
else:
    print("That item is NOT available")