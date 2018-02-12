#!/usr/bin/env python

user_submitted = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+{}|\';?/.,><\""

verify_arr = [193, 35, 9, 33, 1, 9, 3, 33, 9, 225]

password = ""

for verify_char in verify_arr:
    for char in user_submitted:
        newchar = ( (((ord(char) << 5) | (ord(char) >> 3)) ^ 111) & 255 )
        if(newchar == verify_char):
            #print "letter found! "+char
            password += char

print "The password is: "+password
