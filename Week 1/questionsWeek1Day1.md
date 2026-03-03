
### Day 1 :
### Level 1: Easy (The Fundamentals)
*Focus: Basic loops, conditionals, list/string methods, and simple functions.*

1. **The Sum of Evens:** Write a function that takes an integer $N$ and returns the sum of all strictly even numbers from 1 to $N$.
2. **Palindrome Checker:** Write a function that returns `True` if a string reads the same forwards and backwards (ignoring spaces and case), and `False` otherwise.
3. **List Reverser:** Reverse a list of numbers *without* using Python's built-in `.reverse()` method or `[::-1]` slicing.
4. **Character Frequency:** Take a string and return a dictionary counting how many times each character appears.
5. **Find the Missing Number:** Given a list containing $n$ distinct numbers taken from $0, 1, 2, ..., n$, find the one that is missing from the list.
6. **Celsius to Fahrenheit:** Write a function that converts a list of Celsius temperatures into a new list of Fahrenheit temperatures using a list comprehension.
7. **Remove Duplicates:** Write a function thae keeping the original order of elements intact (don't just convert to a set, as sets lose order).t removes duplicate elements from a list whil
8. **Factorial Calculator:** Write a function using a `while` loop to calculate the factorial of a given number $N$ (e.g., $5! = 5 \times 4 \times 3 \times 2 \times 1$). 
9. **Vowel Remover:** Write a function that takes a string and returns a new string with all the vowels removed.
10. **Target Search:** Iterate through a list of integers. If you find the number `7`, print its index and stop the loop. If `7` is not in the list, print "Not found".

---

### Day3
### Level 2: Medium (Data Structures & Logic)
*Focus: Dictionaries, sets, nested loops, two-pointer techniques, and intermediate algorithms.*

11. **Anagram Checker:** Write a function that takes two strings and returns `True` if they are anagrams (contain the exact same letters in the exact same quantities).
12. **The "Two Sum" Problem:** Given a list of integers and a `target` sum, return the *indices* of the two numbers that add up to the target.
13. **Balanced Parentheses:** Write a function that takes a string of brackets (e.g., `"{[()]}"`) and returns `True` if they are matched and nested correctly, using a List as a "Stack".
14. **First Non-Repeating Character:** Find and return the first character in a string that occurs only once. If all characters repeat, return `None`.
15. **Merge and Sum Dictionaries:** Given two dictionaries with string keys and integer values, merge them. If a key exists in both, add their values together.
16. **Matrix Transpose:** Given a 2D list (a list of lists representing a grid), write a function to swap its rows and columns.
17. **Group Anagrams:** Given a list of words (e.g., `["eat", "tea", "tan", "ate", "nat", "bat"]`), group the anagrams together into a list of lists.
18. **Pangram Checker:** Write a function to check if a sentence contains every letter of the English alphabet at least once. (Hint: Sets make this incredibly easy).
19. **Prime Number Generator:** Write a function that generates a list of all prime numbers up to a given integer $N$.
20. **Run-Length Encoding:** Compress a string by replacing sequences of the same character with the character followed by its count (e.g., `"AABBBCCAA"` becomes `"A2B3C2A2"`).

---

### Day 3
### Level 3: Hard (Optimization & Advanced Concepts)

*Focus: Time/space complexity, sliding windows, recursion, and complex array manipulation.*

21. **Binary Search:** Write a function to find the index of a target value in a *sorted* list by repeatedly dividing the search interval in half.
22. **Longest Substring Without Repeating Characters:** Given a string, find the length of the longest substring without repeating characters using the "sliding window" technique.
23. **Flatten a Nested List (Recursion):** Write a recursive function that takes a deeply nested list (e.g., `[1, [2, [3, 4], 5]]`) and returns a completely flat list (`[1, 2, 3, 4, 5]`).
24. **Merge Overlapping Intervals:** Given a list of intervals (e.g., `[[1,3], [2,6], [8,10]]`), merge any overlapping intervals and return the condensed list (`[[1,6], [8,10]]`).
25. **Sudoku Board Validator:** Given a 9x9 grid of numbers (and blanks), write a function that verifies if the current board state is valid according to Sudoku rules (no duplicates in rows, columns, or 3x3 sub-boxes).
26. **Trapping Rain Water:** Given a list of non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
27. **Least Recently Used (LRU) Cache:** Simulate an LRU cache. Write a class that has a fixed capacity. When it gets full, adding a new item should remove the item that was accessed the longest time ago.
28. **Coin Change (Dynamic Programming approach):** Given a list of coin denominations and a total amount, write a function to find the *minimum* number of coins needed to make up that amount.
29. **Valid Tic-Tac-Toe State:** Given a 3x3 grid containing 'X', 'O', and ' ' (blank), return `True` if it represents a valid board state that could actually be reached during a real game.
30. **Spiral Matrix:** Given an $m \times n$ matrix, return all elements of the matrix in spiral order (starting from top-left, going right, down, left, up, and repeating inward).

