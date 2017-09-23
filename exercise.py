"""
Exercsie 1:
Write a Python function that checks whether a passed string is palindrome or not.
Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.

Exercise 2:
Write a Python function to check whether a string is pangram or not.
Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"
Hint: Look at the string module

Exercise 3:
Write a Python function that takes a list and returns a new list with unique elements of the first list.
Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
"""
# Solution to exercise 1
word = input("Enter word:")
reverse = word[::-1]

if word == reverse:
    print("It's a palindrome")

else:
    print("Not palindrome")
#

#Solution to exercise 2


#Random Solution
peoples = ['Francis', 'Andrew', 'Pascal', "Edem"]
countries = ['Ghana', 'USA', 'Congo', "Ghana"]

for person, country in zip(peoples, countries):
    print(person, country)