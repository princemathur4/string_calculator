# String Calculator Implementation using TDD
## Project Description
A simple calculator which takes in a string containing numbers and returns the sum of those numbers in output
Implemented in TDD fashion (Test driven development)

## Features implemented:
- [x] Handles empty string → Returns 0.
- [x] Handles single and multiple comma-separated numbers → Returns their sum.
- [x] Supports newline (\n) as a delimiter → "1\n2,3" returns 6.
- [x] Supports custom delimiters → Example: "//;\n1;2" returns 3.
- [x] Throws an exception for negative numbers → "negative numbers not allowed -1".
- [x] Handles multiple negative numbers in the error message → "negative numbers not allowed -1,-2".

## Instructions to run:
- Install Python3.10 
- Install dependencies from requirements.txt file using this command: `pip install -r requirements.txt`
- Run code via: `StringCalc.add("<string containing numbers>")` 
- Run tests via: `pytest test_string_calc.py`

## How is it tested?
- [x] Unit Tested

### Testcases
- [x] **Method existence** → Ensures the `add` method exists in `StringCalc`.  
- [x]  **Non-string input handling** → Raises an exception when input is not a string.  
- [x]  **Empty string handling** → Returns `0` when input is an empty string.  
- [x]  **Basic addition (1,2)** → Returns `3` for input `"1,2"`.  
- [x]  **Basic addition (3,4)** → Returns `7` for input `"3,4"`.  
- [x]  **Newline delimiter support** → Returns `6` for `"1\n2,3"`.  
- [x]  **Custom delimiters (`;`)** → Returns `3` for `"//;\n1;2"`.  
- [x]  **Custom and newline delimiters (`;` and `\n`)** → Returns `6` for `"//;\n1;2\n3"`.  
- [x]  **Invalid delimiters** → Raises an exception for unsupported delimiters like `"//;\n1.2\n3"`.  
- [x]  **Single negative number handling** → Raises an exception with `"Negative numbers not allowed: [-2]"`.  
- [x]  **Multiple negative numbers handling** → Raises an exception listing all negative numbers (`"Negative numbers not allowed: [-2,-3,-5]"`).  

## PR and Commits
https://github.com/princemathur4/string_calculator/pull/1/commits
