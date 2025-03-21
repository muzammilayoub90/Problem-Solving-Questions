#Write a function that takes a string as input and returns the reversed string.
def reverse_string(s):
    return s[::-1]

input_str ="hello"
output_str = reverse_string(input_str)
print(output_str)

#Write a function that counts the number of vowels (a,e,i,o,u) in a string (case-insensitive).
def count_vowels(s):
    vowels = {"a","e","i","o","u"}
    count = 0

    for char in s.lower():
        if char in vowels:
            count += 1
    return count
print("Total vowels:",count_vowels("Apple"))
print("Total vowels:",count_vowels("ORANGE"))

#Write a function that takes a non-negative integer and returns the sum of its digits.
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

print(sum_of_digits(1234))