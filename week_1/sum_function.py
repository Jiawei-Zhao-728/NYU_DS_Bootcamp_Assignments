# Exercise 5: Sum Function
# Write a function sum_of_integers(a, b) that takes two integers as input from the user and returns their sum. (optional)


def sum_of_integers(a, b):
    return a + b


def main():
    a = int(input("Enter the first integer: "))
    b = int(input("Enter the second integer: "))
    sum = sum_of_integers(a, b)
    print(f"The sum of {a} and {b} is {sum}.")
    return sum

if __name__ == "__main__":
    main()
