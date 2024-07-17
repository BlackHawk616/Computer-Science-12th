# writing a program to read the content of file and display "E" in place of "I" while displaying the content of file all other ccharacters should appear as it is

f = open("//home//blackhawk//School//Class 12//Computer Science//Practicals Programs//Text Files//sample2.txt", "r")

contet = f.read()

l = len(contet)

new_Content = contet.replace("I", "E")

print(new_Content)
    
