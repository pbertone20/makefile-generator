---SAMPLE RUN---
<pre>
<code>
Enter filenames (e.g. fun1.c fun2.c ...): fun1.c fun2.c fun3.c
Enter main (e.g. funMain.c): funMain.c
Enter exe filename (e.g. fun): fun
Enter header filename (e.g. fun.h): funHeader.h
Enter compiler (e.g. gcc): gcc 
Enter flags (e.g. -std=c99 -Wall ...): -std=c99 -Wall

----------BEGIN MAKEFILE----------

fun: fun1.o fun2.o fun3.o funMain.o funHeader.h
        gcc -std=c99 -Wall fun1.o fun2.o fun3.o funMain.o -o fun
funMain.o: funMain.c funHeader.h
        gcc -std=c99 -Wall -c funMain.c
fun1.o: fun1.c funHeader.h
        gcc -std=c99 -Wall -c fun1.c
fun2.o: fun2.c funHeader.h
        gcc -std=c99 -Wall -c fun2.c
fun3.o: fun3.c funHeader.h
        gcc -std=c99 -Wall -c fun3.c
clean:
        rm *.o fun
----------END MAKEFILE----------

Time taken = 0.0008192062377929688
</code>
</pre>
