# Exercise 4: Palindrome Checker
# Write a program to check if a string is a palindrome or not.

def main():
    string = input("Enter a string: ")
    if string == string[::-1]:
        print(f"The string '{string}' is a palindrome.")
    else:
        print(f"The string '{string}' is not a palindrome.")
    return string

if __name__ == "__main__":
    main()
