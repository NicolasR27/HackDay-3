
# ASCII string 
inp_text = input("Enter a string of ASCII characters:")
# list of ascii values of each char in string
ascii_list = []
# ascii list encoded to DNA characters
encoded_list = []

# Generate the DNA dictionary for the 255 ASCII characters
# The dictionary will have 255 entries, the key will be the ASCII value of
# a character. The value will be the 4-character DNA value.


# To convert the string to ascii/binary (if binary is needed)
def convert_ascii(ascii_string):
  for char in ascii_string:
     ascii_list.append(ord(char))


convert_ascii(inp_text)  
print (ascii_list)



