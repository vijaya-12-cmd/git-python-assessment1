def is_palindrome(text):
  # Convert the string to lowercase for case-insensitive comparison
  text = text.lower()
  # Use string slicing to reverse the text
  reversed_text = text[::-1]
  # Compare the original and reversed strings
  return text == reversed_text

# Example Usage
print(is_palindrome("madam"))
print(is_palindrome("Racecar"))
print(is_palindrome("hello"))
print(is_palindrome("A man a plan a canal Panama"))