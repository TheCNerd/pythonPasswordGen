"""
GPLv2 or later License.
You may freely copy, distribute,
edit, run it, etc.

Basically:
Do whatever you want with it.


Unfortunately, I have to do the decision 
making Tsundere style because Python doesn't
have switch statements like most other languages do.
"""

# Import the necessary libraries 
import random
import time
import string

# Print the obvious
print("This is a password creator.")

# Prompt the user on what kind of password he/she would like. The input is stored in variable 't'
t = input("what type of password would you like?\nA. Numbers?\nB. Letters?\nC. Numbers and Letters?\nD. Numbers,Letters, and Special Characters?\n")

# The different passwords types
w= "Numbers"
x= "Letters"
y= "Numbers and Letters"
z= "Numbers, Letters, and Special Characters"

"""
These are just if the user either enters the letter associated 
with the type or if he/she type in the type he/she wants.
"""
if t.lower() == w.lower() or t.lower() == 'a':
    k=input ("How many characters do you want in your password?")
    chars=string.digits
    print("Your Password Is...")
    print(''.join(list(random.choices(chars, k=int(k)))))
elif t.lower() == x.lower() or t.lower() == 'b':
    k=input ("How many characters do you want in your password?")
    chars = string.ascii_uppercase + string.ascii_lowercase
    print("Your Password Is...")
    print(''.join(list(random.choices(chars, k=int(k)))))
elif t.lower() == y.lower() or t.lower() == 'c':
    k=input ("How many characters do you want in your password?")
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    print("Your Password Is...")
    print(''.join(list(random.choices(chars, k=int(k)))))
elif t.lower() == z.lower() or t.lower() == 'd':
    k=input ("How many characters do you want in your password?")
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    print("Your Password Is...")
    print(''.join(list(random.choices(chars, k=int(k)))))

# Sleep so the user has time to copy the password.
time.sleep(30)
