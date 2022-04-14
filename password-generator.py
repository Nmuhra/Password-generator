import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = uppercase_letters.lower()
digits = "0123456789"
symbols = "(){}[],./\\?+=*# "

upper, lower, nums, syms = True, True, True, True

all = ""

print("Here are some passwords!")

if upper :
    all += uppercase_letters
if lower :
    all += lower_case
if nums :
    all += digits
if syms :
    all += symbols
length_1 = input("length: ")
length = int(length_1)
amount_1 = input("amout: ")  
amount = int(amount_1)

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)
