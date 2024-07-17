# WAP to read content of file and display how many upper case characters and digits are present

f = open("//home//blackhawk//School//Class 12//Computer Science//Practicals Programs//Text Files//sample3.txt","r")

content = f.read()

l = len(content)

upper = 0

digit = 0

for i in content:

    if i.isupper():
        upper +=1

    elif i.isdigit():
        digit += 1

print("The No. Of Upper Case are : ", upper)

print("The No. Of digits are : ", digit)

