def sum_of_digits():
    total = 0
    number = float(input("Enter the numbers to be added: "))
    while number > 0:
        total += number
        number = float(input("Enter the numbers to be added: "))
    return total
print(sum_of_digits())
