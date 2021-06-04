from des import test_1_keys
from test_des import *
from helpers import task2_k_1, task2_k_2


def main():
    # Test 1
    # encyption and decryption
    plain_t, cipher_t = test_1()
    for i in range(len(task1_keys)):
        print("Key: {}, and the cracked plain text is: {}.\
            ".format(plain_t[i], cipher_t[i])) 
    
    # Test 2
    plain_t2, cipher_t2 = test_2()
    for i in range(len(task2_k_1)):
        print("Key 1: {}, key 2: {}, and the cracked plain text is: {}.\
            ".format( task2_k_1[i], task2_k_2[i], cipher_t2[i]))
    
    # Test 3
    test3_1()
    test3_2()



if __name__ == "__main__":
    main()
