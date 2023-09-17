# DSA-week1-code-challenge
# Data Structures and Algorithms

This repository contains three Python functions that demonstrate the use of different data structures:

1. **Stacks**:
   - Function: `is_balanced(expression)`
   - Description: Checks if a given expression containing parentheses, curly braces, and square brackets is balanced. An expression is considered balanced if each opening bracket has a corresponding closing bracket in the correct order.
   - Sample Usage:
     ```python
     expression1 = "([]{})"
     expression2 = "([)]"
     print(is_balanced(expression1))  # Output: True
     print(is_balanced(expression2))  # Output: False
     ```

2. **Sequences (Lists/Tuples)**:
   - Function: `remove_duplicates(sequence)`
   - Description: Removes duplicates from a given sequence (list or tuple) while preserving the original order of elements.
   - Sample Usage:
     ```python
     input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
     result = remove_duplicates(input_sequence)
     print(result)  # Output: [2, 3, 4, 5, 6, 7]
     ```

3. **Dictionaries**:
   - Function: `word_frequency(sentence)`
   - Description: Calculates the frequency of each word in a given sentence, ignoring punctuation and considering words in a case-insensitive manner.
   - Sample Usage:
     ```python
     sentence = "This is a test sentence. This sentence is a test."
     result = word_frequency(sentence)
     print(result)
     ```

Feel free to use these functions in your Python projects by importing them and following the provided sample usage. These functions can help you solve various common problems related to data structures and algorithms.

