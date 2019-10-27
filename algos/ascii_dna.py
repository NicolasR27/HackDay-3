
# ASCII string 
inp_text = input("Enter a string of ASCII characters:")
# list of ascii values of each char in string
ascii_list = []
# Binary numbers converted to strings
binary_list = []
# ascii list encoded to DNA characters
encoded_list = []
# Dict to hold DNA constants
dna_const = {'00':'A', '01':'T', '10':'G', '11':'C'}

# function to convert binary numbers into DNA encoded value
def encode_bin(bin_string):
  bin_string = bin_string[2:]
  while len(bin_string) < 8:
    bin_string = '0' + bin_string
  bin_list = []
  for i in range(4):
    bin_list.append(bin_string[:2])
    bin_string = bin_string[2:]
  for item in bin_list:
    if item == '00':
      encoded_list.append('A')
    elif item == '01':
      encoded_list.append('T')
    elif item == '10':
      encoded_list.append('G')
    else:
      encoded_list.append('C')


 # print(bin_list)

    

# To convert the string to ascii/binary (if binary is needed)
def convert_ascii(ascii_string):
  for char in ascii_string:
    ascii_list.append(ord(char))
  for item in ascii_list:
    binary_list.append(str(bin(item)))
  for item in binary_list:
    encode_bin(item)

convert_ascii(inp_text)  
# print (ascii_list)
# print (binary_list)
# print (encoded_list)

encoded_string = ""
for item in encoded_list:
  encoded_string = encoded_string + item

print(encoded_string)

