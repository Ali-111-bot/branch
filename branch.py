hours = int(input("Enter KW hours used: "))

first = 7.633
second = 9.259

if hours <= 1000:
    total = hours * first
else:
    total = (first * 1000) + ((hours - 1000) * second)

total = total / 100
print("The amount you owe is: $", total)



