
task1_keys = [ "0000000000", "0000011111", "0010011111","0010011111", "1111111111", "0000011111","1000101110","1000101110"]
task1_pt = ["00000000", "11111111", "11111100", "10100101"]
task1_ct = ["00001111","01000011","00011100","11000010"]

task2_k_1 = ["1000101110", "1000101110", "1111111111", "0000000000", "1000101110", "1011101111", "1111111111", "0000000000"]
task2_k_2 = ["0110101110", "0110101110", "1111111111", "0000000000","0110101110", "0110101110", "1111111111", "0000000000"]
task2_pt = ["11010111", "10101010", "00000000", "01010010"]
task2_ct = ["11100110", "01010000", "00000100", "11110000"]


def left_shift(bits, shift):
    return bits[shift:] + bits[:shift]

# This method XOR the expansion permutated L-block with the sk
def xor_bit(c0,c1, block_length = 8):
    xor_ep_sk = ""
    for i in range(block_length):
        if (c0[i] == c1[i]):  
            xor_ep_sk += "0"
        else:  
            xor_ep_sk += "1"
    return xor_ep_sk

# This method converts the decrypted messages from bits to bytes
def convert_to_txt(bits, encoding='utf-8', errors='surrogatepass'):
    try:
        n = int(bits, 2)
        enc = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'
        return True, enc
    except Exception as e:
        return False, e

# Read the file which contains the cipher text
def read_f(file_name):
    cipher_txt = ""
    try:
        with open(file_name, "r") as cipher:
            cipher_txt = cipher.read()
    except IOError:
        return "Could not find the file!"
    return cipher_txt


# This method writes the encypted text to a file
def write_file(file_name, txt):
    cipher_txt = ""
    try:
        with open(file_name, "a") as cipher:
            
            cipher_txt = cipher.write(txt +'\n')
        if cipher_txt != len(txt):
            return "Something went wrong!"
    except IOError:
        return "Could not find the file!"

    return "Successfully wrote the cipher text to the file"
