text = 'Plain text'
key = 3

# creating a function called encryption
# which would take in two arguments, the 
# text and key
def encryption(text,key):
    # initializing a variable to store 
    # the encrpyted message
    encrypted_message = ""
    
    # initializing a variable that would help 
    # tell where to start and end according to 
    # the key
    start = 0
    
    # the algorithm here is to loop through the key
    # and while doing that loop through the text in a 
    # gap of the key. For eg if the key = 2, we loop through 
    # the text in steps of 2 and add the characters into the 
    # storing variable
    while start < key:
        for j in range(start,len(text),key):
#             adding the characters gotten in the steps of 
#             the key
            encrypted_message += text[j]
#         incrementing the start variable so that it start from the
#         next index to take the steps of the key
#         till it equals key.
        start += 1

    # return the answer gotten from the encryption
    return encrypted_message

encrypted = encryption(text,key)


# creating a function decryption with two
# arguments text an key
def decryption(encrypted,key):
    # initializing variables needed for the program
    a = 0
    decrypted_message = ''
    
#     checking for edges cases when the length of the 
#     text is even and the key is even 
    if len(encrypted) % 2 == 0 and key % 2 == 0: 
        # dividing the length of the word by the key to
        # know which partitions to start from 
        b = len(encrypted)//key 
        
        # while a in less than the partition
        while a < b:
            # loop through the length of the word starting at
            # a and take b steps every time
            for i in range(a,len(encrypted),b):
                # adding the characters to our result variable
                decrypted_message += encrypted[i]
            # incrementing a to start at the next index
            # and take b steps every time
            a+=1 
            
    # checking for edges cases when the length of the 
    # text is even and the key is odd   
    if len(encrypted) % 2 == 0 and key % 2 != 0:
        # dividing the length of the word by the key to
        # know which partitions to start from
        b = len(encrypted)//key 
        
        # while a in less than the partition
        while a < b:
            b += 1
            # adding the characters to our result variable
            decrypted_message += encrypted[a] 
#             loop through the length of the word starting at
#             a 
            for i in range(a,len(encrypted)):
                # getting the next index to add to the answer
                c = i + b
                decrypted_message += encrypted[c]
                # getting the next index to add to the answer
                decrypted_message += encrypted[c+key]
                # breaking out of the loop
                break
                
            # reset the b to the partition
            b = len(encrypted)//key 
            # increment incrementing a to start at the next index
            # and take b steps every time
            a+=1 
        # add the last character of b to the answer
        decrypted_message+= encrypted[b]

    # return decrypted_message
    return decrypted_message
# calling the function
decrypted = decryption(encrypted,key)

print("The plain text is: " + text)
print("The text after encryption is: "+ encrypted)
print("The text after decryption is: "+ decrypted)

