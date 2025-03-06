def reverse_binary(binary_string):
    return binary_string[::-1]

def string_to_binary(input_string):
    return ''.join(format(ord(char), '08b') for char in input_string)

def binary_to_string(binary_string):
    char_array = [chr(int(binary_string[i:i+8], 2)) for i in range(0, len(binary_string), 8)]
    return ''.join(char_array)

def string_to_hex(s):
    return hex(int.from_bytes(s.encode(), 'big'))

def mystery_conversion(hex1):
    sum = int(hex1, 16) + 0x1F
    return hex(sum)

def hex_to_binary(hex_str):
    hex_str = hex_str[2:]
    decimal = int(hex_str, 16)
    return bin(decimal)[2:]

def encrypt(input):
    step1 = string_to_hex(input)
    step2 = mystery_conversion(step1)
    step3 = hex_to_binary(step2)
    return reverse_binary(step3)
    

secret = "1111001001110110101010100010110000110110101011100010110011100110011101101000110001001110101001101010011001110110100011001110011001110110101000101100110011001110010011101100110001101110110011000100101"
input = input("Digite um código: ")
encrypted = encrypt(input)
if encrypted == secret:
   print("Sucesso!")
else:
   print("Falha...")


