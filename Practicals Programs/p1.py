# Writing a program to read the content of file and count how many time letter "a" comes in file

f = open("//home//blackhawk/School//Class 12//Computer Science//Practicals Programs//Text Files//sample1.txt")

content = f.read()

l = len(content)

count = 0

for i in range(l):

    if content[i] == "a":

        count += 1

print("The total count of letter a is : ", count)
