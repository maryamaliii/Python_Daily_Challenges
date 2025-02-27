# Daily python challenge Day_04
# Q: Write a Python program that converts a number to words.
# Example: 1234 => one thousand two hundred thirty four
 
from num2words import num2words

num = input("Enter your Number : ")
words = num2words (int(num))
print("Your Answer :", words)