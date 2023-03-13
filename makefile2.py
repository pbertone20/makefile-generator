#usr/bin/env/python3
import time

string = input("Enter filenames (e.g. fun1.c fun2.c ...): ").split()
main = input("Enter main (e.g. funMain.c): ")
objStr = [str[:-2] + ".o" for str in string]
objMain = main[:-2] + ".o"
exe = input("Enter exe filename (e.g. fun): ")
head = input("Enter header filename (e.g. fun.h): ")
compiler = input("Enter compiler (e.g. gcc): ");
flags = input("Enter flags (e.g. -std=c99 -Wall ...): ").split()

t0 = time.time()

with open("makefile", "w") as makefile:
    makefile.write(f"{exe}: {' '.join(objStr)} {head}\n")
    makefile.write(f"\t{compiler} {' '.join(flags)} {' '.join(objStr)} -o {exe}\n")
    
    makefile.write(f"{objMain}: {main} {head}\n")
    makefile.write(f"\t{compiler} {' '.join(flags)} -c {main}\n")
    
    for obj, src in zip(objStr, string):
        makefile.write(f"{obj}: {src} {head}\n")
        makefile.write(f"\t{compiler} {' '.join(flags)} -c {src}\n")
    
    makefile.write("clean:\n")
    makefile.write(f"\trm *.o {exe}\n")

print(f"Time taken = {time.time() - t0}")