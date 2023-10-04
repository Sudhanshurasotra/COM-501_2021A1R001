string = "Welcome to Python"

alphabet_count = sum(c.isalpha() for c in string)
print("Number of alphabets in the given string:", alphabet_count)

start_index = 2
end_index = 8
extracted_chars = string[start_index:end_index + 1]
print("Extracted characters from index 2 to 8:", extracted_chars)

is_alphanumeric = string.isalnum()
print("Is the string alphanumeric?", is_alphanumeric)