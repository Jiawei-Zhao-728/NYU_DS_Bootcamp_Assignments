# Exercise 1: Vowel Counter
# Write a program that takes a word as an input and prints the number of vowels in the word.

def vowel_counter(word):
    vowels = 'aeiouAEIOU'
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    
    return count

def main():
    # get user input
    word = input("Enter a word: ")
    vowel_count = vowel_counter(word)

    # Print result
    print(f"The word '{word}' has {vowel_count} vowel(s).")



if __name__ == "__main__":
    main()
