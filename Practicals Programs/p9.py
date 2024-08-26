# Write A Python Program To Write those lines which has character "p" from one text file to another 

def copyfiles(file1, file2):
    with open(file1, "r") as f1:
        with open(file2, "w") as f2:
            for lines in f1:
                if 'p' in lines:
                    f2.write(lines)
    print("Lines With P  are copied to new file")

f = "Text Files/file1.txt"
f_2 = "Text Files/file2.txt"

copyfiles(f,f_2)