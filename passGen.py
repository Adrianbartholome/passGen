import random
import string

length = int(input("Enter length requirement (5 to 20): "))

lower = upper = spec = num = pw = ""

if (length in range(5, 21)):
    divs = round(length / 4)
    divs2 = round(divs / 2)
    if (divs2 == 0):
        divs2 = 1

    for i in range(divs):
        lower += random.choice(string.ascii_lowercase)
        upper += random.choice(string.ascii_uppercase)
    for i in range(divs2):
        num += str(random.choice(string.digits))
        spec += str(random.choice(string.punctuation))

else:
    length = int(input("Please enter a valid number: "))

temp = str(lower + upper + num + spec)
remain = length - len(temp)
for i in range(remain):
    temp += random.choice(string.punctuation)

w = []
for i in temp:
    w.append(i)
random.shuffle(w)
for i in w:
    pw += i

print(pw)