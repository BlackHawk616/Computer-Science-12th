# Writing a program to read the content offile and count how many vowels in it.

def vowels(path):

    try:
        f = open(path, "r")
        content = f.read()
        l = len(content)
        vowel = 0

        for char in content:
            if char in ["a","e","i","o","u"]:
                vowel += 1
        print("Total Vowels are : ", vowel)
    except Exception as e:
        print(e)

vowels("//home//blackhawk/School//Class 12//Computer Science//Practicals Programs//Text Files//sample4.txt")