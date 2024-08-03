def is_palindrome(s):
  """
  Checks if a given string is a palindrome.

  Args:
    s: The string to check.

  Returns:
    True if the string is a palindrome, False otherwise.
  """

  s = s.lower()  # Case-insensitive comparison
  s = ''.join(filter(str.isalnum, s))  # Remove non-alphanumeric characters

  return s == s[::-1]

# Get input from the user
input_string = input("Enter a string: ")

# Check if the string is a palindrome
if is_palindrome(input_string):
  print("The string is a palindrome.")
else:
  print("The string is not a palindrome.")