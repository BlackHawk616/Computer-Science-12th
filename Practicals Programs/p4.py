# Writing a program to read the content offile and count how many vowels in it.

def vowels(path):

    try:
        f = open(path, "r")
        content = f.read()
        l = len(content)
        vowel = 0

        for i in range(l):

            if content[i] == "a":
                vowel +=1

            elif content[i] == "e":
                vowel +=1

            elif content[i] == "i":
                vowel +=1
            
            elif content[i] == "o":
                vowel +=1

            elif content[i] == "u":
                vowel +=1
        print("Total Vowels are : ", vowel)
    except Exception as e:
        print(e)

vowels("//home//blackhawk/School//Class 12//Computer Science//Practicals Programs//Text Files//sample4.txt")