from part2_helpers import *
from itertools import product
import binascii

# This method produces the subkeys k1 and k2
def produce_subkeys(ten_bit_key):
    p10 = [ten_bit_key[2], ten_bit_key[4], ten_bit_key[1], ten_bit_key[6] , ten_bit_key[3],\
     ten_bit_key[9], ten_bit_key[0], ten_bit_key[8], ten_bit_key[7], ten_bit_key[5]]
    LS_1_1 = []
    LS_1_2 = []
    # Devide the key into to 5 bits
    for i in range(0,5):
        LS_1_1.append(p10[i])
        LS_1_2.append(p10[i+5])
    # Do a shift operation on the each first key of the two half of the keys
    LS_1_1_shift = left_shift(LS_1_1, 1)
    LS_1_2_shift = left_shift(LS_1_2, 1)
    
    # Putting toghether the two part after the shifting, to do the P8 and then produce the k1 
    connect_ls = LS_1_1_shift + LS_1_2_shift  
    key1_p8 = [connect_ls[5], connect_ls[2], connect_ls[6], connect_ls[3], connect_ls[7], connect_ls[4], connect_ls[9], connect_ls[8]] 
    # Do two left shift operation on the already shifted LS_1
    LS_2_1_shift = left_shift(LS_1_1_shift,2)
    LS_2_2_shift =left_shift(LS_1_2_shift, 2)    
    # Putting toghether the two part after the shifting, to do the P8 and then to produce the k2
    connect_ls2 = LS_2_1_shift + LS_2_2_shift  
    key2_p8 = [connect_ls2[5], connect_ls2[2], connect_ls2[6], connect_ls2[3], connect_ls2[7], connect_ls2[4], connect_ls2[9], connect_ls2[8]] 
    # Convert the keys to string 
    key_1 = ''.join(key1_p8)
    key_2 = ''.join(key2_p8)

    return key_1, key_2


# This method does the Intial Permutation of the 8-bit block of plain text
def ip(pt_8bit):
    permute = [pt_8bit[1], pt_8bit[5], pt_8bit[2], pt_8bit[0], pt_8bit[3], pt_8bit[7], pt_8bit[4], pt_8bit[6]]
    ip_8bit = ''.join(permute)
    return ip_8bit

# This method does the Inverse Intial Permutation of the 8-bit block the encypted plain text
def inv_ip(pt_8bit):
    inv_permute = [pt_8bit[3], pt_8bit[0], pt_8bit[2], pt_8bit[4], pt_8bit[6], pt_8bit[1], pt_8bit[7], pt_8bit[5]]
    inv_ip_8bit = ''.join(inv_permute)
    return inv_ip_8bit

# This method encypts the permuted 8-bit block plain text
def f_k(block_8bit, sk):
    # Devide the permuted 8-bits block in to L and R block of 4-bits
    l_bits = block_8bit[0:4]
    r_bits = block_8bit[4:]
    # The R 4-bits sends to the mapping function F
    p4_F = f(r_bits, sk)
    # xor the 4 bits of the P4 and the Left 4-bit of the block
    p4_xor_left = xor_bit(l_bits,p4_F, 4)
    
    return p4_xor_left, r_bits


# This method takes the right most 4-bits of the input in the f_k function to do the expansion, permutation, and the S blocks operations
def f(r_b, sk):
    # Expansion/Permutation operation
    ep = [r_b[3], r_b[0], r_b[1], r_b[2], r_b[1], r_b[2], r_b[3], r_b[0]]
    xor_ep_sk = xor_bit(ep,sk)
    # Devide the xored bits in to two list of 4 bits with the entries P_x,x 
    s0_bits = xor_ep_sk[0:4]
    s1_bits = xor_ep_sk[4:]
    s0_2bits_result = s0_box(s0_bits)
    s1_2bits_result = s1_box(s1_bits)
    # Sum the 2 bits from s0 and s1, and do the P4 operaion
    p4_initalize = s0_2bits_result + s1_2bits_result
    p4 = [p4_initalize[1], p4_initalize[3], p4_initalize[2], p4_initalize[0]]
    return p4

# The swich method, switches the left and right side  
def switch(left, right):
    sw = right + left
    return sw

# S0 box
def s0_box(s0_bits):
    s0_box = [[1,0,3,2],
            [3,2,1,0],
            [0,2,1,3],
            [3,1,3,2]]
    # find the S0 row and col numbers in base 2
    row = int(s0_bits[0]+s0_bits[3],2)
    col = int(s0_bits[1]+s0_bits[2],2)
    idx = s0_box[row][col] 
    # The converion to bit returns 1 bit for value 0 or 1 from matrix 
    idx_binary = format(idx,'b') 
    if len(idx_binary) == 1:
        idx_binary = '0'+idx_binary
    return idx_binary

# S1 box
def s1_box(s1_bits):
    s1_box = [[0,1,2,3],
        [2,0,1,3],
        [3,0,1,0],
        [2,1,0,3]]
    # find the S1 row and col numbers in base 2
    row = int(s1_bits[0]+s1_bits[3], 2)
    col = int(s1_bits[1]+s1_bits[2], 2)
    idx = s1_box[row][col]
    # The converion to bit returns 1 bit for value 0 or 1 from matrix 
    idx_binary = format(idx,'b')
    if len(idx_binary) == 1:
        idx_binary = '0'+idx_binary
    return idx_binary


# This method encrypt the plain text
def encryption(sk1,sk2, p_txt):
    init_permutaion = ip(p_txt)
    l1, r1 = f_k(init_permutaion, sk1)
    sw = switch(l1,r1)
    l2, r2 = f_k(sw, sk2)
    f_k_result = l2+r2
    encrypt = inv_ip(f_k_result) 
    return encrypt

# This method dencrypt the cipher text
def decryption(sk1,sk2, c_txt):
    init_permutaion = ip(c_txt)
    l1, r1 = f_k(init_permutaion, sk2)
    sw = switch(l1, r1)
    l2, r2 = f_k(sw, sk1)
    fk_result = l2+r2
    plain_text = inv_ip(fk_result)
    return plain_text
 



