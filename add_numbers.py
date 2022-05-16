numbers_to_add = int(input("Enter how many numbers you want to add: "))

sum = 0
counter = 1

while counter <= numbers_to_add:
    number = int(input("Enter a number to add: "))
    sum = sum + number
    counter = counter + 1

print("The sum is", sum)