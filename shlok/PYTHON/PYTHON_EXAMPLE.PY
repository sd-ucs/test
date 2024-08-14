# Explicit Line Joining Example

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("All numbers:", numbers)

print("Numbers divisible by 2 and 3:")
for num in numbers:
    if num % 2 == 0 and num % 3 == 0:
        print("Item:", num)