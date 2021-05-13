name = input("Enter your name:")
marks = input("Enter your marks:")
number = input("Enter your number:")


template = "The name of the student is {}, his marks are {} and phone number is {}"


output = template.format(name, marks, number)
print(output)