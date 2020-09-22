import random
import time
import string

print("This is a password creator.")
t=input("what type of password would you like?\nA. Numbers?\nB. Letters?\nC. Numbers and Letters?\nD. Numbers,Letters, and Special Characters?\n")

w= "Numbers"
x= "Letters"
y= "Numbers and Letters"
z= "Numbers, Letters, and Special Characters"

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

time.sleep(30)