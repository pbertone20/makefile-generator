---SAMPLE RUN---
<pre>
<code>
Enter filenames (e.g. fun1.c fun2.c ...): fun1.c
Enter main (e.g. funMain.c): main.c
Enter exe filename (e.g. fun): exe
Enter header filename (e.g. fun.h): header.h
Enter compiler (e.g. gcc): gcc
Enter flags (e.g. -std=c99 -Wall ...): -std=c99 -Wall

----------BEGIN MAKEFILE----------

exe: fun1.o main.o header.h
        gcc -std=c99 -Wall fun1.o main.o -o exe
main.o: main.c header.h
        gcc -std=c99 -Wall -c main.c
fun1.o: fun1.c header.h
        gcc -std=c99 -Wall -c fun1.c
clean:
        rm *.o exe
----------END MAKEFILE----------

Time taken = 0.001035928726196289
</code>
</pre>
