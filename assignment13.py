file1 = open("file.txt","w")
file1.write("Hello \n")
L = ["this is Lovely \n","this is lovely assignment \n","Satya bhalla sir!"]
file1.writelines(L)
file1.close()
file1 = open("file.txt","r+")
print(file1.read())
file1.close()
with open("file.txt") as f:
    with open("copyfile.txt","w") as f1:
        for line in f:
            f1.write(line)
        f1.write("\nthis is copyfile")
f1.close()
f.close()
f1 = open("copyfile.txt","r")
print(f1.read())
f1.close()
with open("file.txt") as f:
    with open("copyfile.txt") as f1:
        with open("combine.txt","w") as f2:
            x = f.readlines()
            y = f1.readlines()
            for line1, line2 in zip(y, x):
                f2.write("{} {}\n".format(line1.rstrip(), line2.rstrip()))
f2.close()
f2 = open("combine.txt","r")
print(f2.read())
