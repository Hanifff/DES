from part2_des import *
from part2_3des import *


# Test 1 -----------------------------------------------------------------------------------------

def test_1():
    keys = task1_keys
    ct = task1_ct
    pt = task1_pt

    for i in range(0,4):
        sk1, sk2 = produce_subkeys(keys[i])
        encrypt = encryption(sk1,sk2,pt[i])
        ct.insert(i,encrypt)

    for i in range(4,8):
        sk11, sk22 = produce_subkeys(keys[i])
        decrypt = decryption(sk11,sk22,ct[i])
        pt.insert(i,decrypt)
    return pt, ct


########################################################################################################
# Test 2 -----------------------------------------------------------------------------------------

def test_2():
    k1 = task2_k_1
    k2 = task2_k_2
    ct = task2_ct
    pt = task2_pt
    for i in range(0,4):
        encrypt = des3_encryption(k1[i],k2[i],pt[i])
        ct.insert(i,encrypt)
    for i in range(4,8):
        decrypt = des3_decryption(k1[i],k2[i],ct[i])
        pt.insert(i,decrypt)
    return pt, ct

########################################################################################################
# Test 3 -1 -----------------------------------------------------------------------------------------

# This method Cracks the des cipher text and stores the cracked key and plain text in file task3_1.txt 
def test3_1():
    ct_msg = read_f("ciphers/CTX1.txt")
    all_keys = list(map(list, product(["0", "1"], repeat=10))) # generate 1024 combination of 10 bits
    cracked_msgs = {}
    cracked_key = ""
    cracked_message = ""
    for i in all_keys:
        crack_des = ""
        key = ''.join(i)
        for j in range(0,len(ct_msg),8):
            cipher_block = ct_msg[j:j+8]
            sk1, sk2 = produce_subkeys(key)
            dec_ct = decryption(sk1,sk2,cipher_block)
            b, encoded = convert_to_txt(dec_ct)
            if b == True:
                crack_des += encoded
        # Regariding to the hint: the message will be 480/8 = 60 length, and it will be a ascii clear msg
        if len(crack_des) == 60 and crack_des.isprintable():
            cracked_message = crack_des
            cracked_key = key
            cracked_msgs[str(i)] = crack_des
            print("The key for the des cipher text is: {}, and the cracked text is: {}.".format(cracked_key, cracked_message)) 
    for k,v in cracked_msgs.items():
        write_file("results\part2_task3_1.txt","The key for the des cipher text is: {}, and the cracked text is: {}.".format(k, v))
    return "Done!"


# Test 3 -2 --------------------------------------------------------------------------------
def test3_2():
    num_cores = multiprocessing.cpu_count()
    print("Running the 3DES dencryption with {} processors.".format(num_cores))
    ct_msg = read_f("ciphers/CTX2.txt")
    #generate 2^20 keys
    all_keys = list(map(list, product(["0", "1"], repeat=20)))
    # using partial function to add other parameter then the one which needed looping (all_keys)
    parallel_proc = partial(parallel_dec, arg2=ct_msg)
    res = Parallel(n_jobs=num_cores, verbose=1)(delayed(parallel_proc)(i)
    for i in all_keys)
    return "Done!"
    
def parallel_dec(i,arg2):
    crack_des = ""
    key1 = ''.join(i[:len(i)//2])
    key2 = ''.join(i[len(i)//2:])
    for j in range(0,len(arg2),8):
        cipher_block = arg2[j:j+8]
        dec_ct = des3_decryption(key1,key2,cipher_block)
        valid, encoded = convert_to_txt(dec_ct)
        #Regarding to the hint: If a byte can not be encoded then the entire sequence will not be valid and we skip to next key combinations
        if valid:
            crack_des += encoded
        if not valid:
            break
     # Regariding to the hint: the message will be 480/8 = 60 length, and it will be a ascii clear msg
    if len(crack_des) == 60 and crack_des.isalpha():
        print("The key for the des cipher text is: {} , and: {}.\n The cracked text is: {}.".format(key1,key2, crack_des))
        write_file("results\part2_task3_2.txt","The keys used to encrypt the 3des cipher text are: {} ,\
             and: {}. The cracked text is: {}.".format(key1,key2, crack_des))
