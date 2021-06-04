from part2_des import *
from joblib import Parallel, delayed
from itertools import product
import multiprocessing 
from functools import partial

# This method use the 3DES encryption method to encrypt the plaintext
def des3_encryption(k1,k2,pt):
    # 1. enc process
    k11,k12 = produce_subkeys(k1)
    enc1 = encryption(k11,k12,pt)
    # 2. dec process
    k21,k22 = produce_subkeys(k2)
    dec2 = decryption(k21,k22,enc1)
    # 3. enc process
    enc3 = encryption(k11,k12,dec2)
    return enc3

# This method use the 3DES decryption method to decrypt the ciphertext
def des3_decryption(k1,k2,ct):
    # 1. dec process
    k11,k12 = produce_subkeys(k1)
    dec1 = decryption(k11,k12,ct)
    # 2. enc process
    k21,k22 = produce_subkeys(k2)
    enc2 = encryption(k21,k22,dec1)
    # 3. dec process
    dec3 = decryption(k11,k12,enc2)
    return dec3
