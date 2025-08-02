#password generator
import random
import string

p1=string.ascii_letters
p2=string.punctuation
p3=string.digits

length=int(input("Enter your password length:"))

combined_ps1=p1+p2+p3
combined_ps=''.join(random.choice(combined_ps1) for _ in range(length))
print("Your generated password is:", combined_ps)
print("Keep it safe!! Do not share to anyone!!")