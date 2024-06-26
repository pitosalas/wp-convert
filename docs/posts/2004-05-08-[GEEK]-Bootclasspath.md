---
title: "[GEEK] Bootclasspath"
author: Pito Salas
date: 2004-05-08
---



In order to debug a hairy problem, I need to step into some Java system  
> classes (hashmap.java) HashMap.class is to be found in rt.jar, part of the  
> standard Java distribution (1.4.2_04) but it does NOT have debug info  
> compiled in.
>>

>> So what to do? I think I did a pretty exhaustive set of steps but I was
still stumped:

>>

>>   * I can't locate an rt.jar with debug info

>>   * From what I read, you can't easily rebuild it from the java system
sources because some stuff does not compile

>>   * I tried recompiling hashmap.java with -g to get debug info and putting
the resulting .class files into a .jar and placing that jar at what I believe
is the front of the classpath. I did this in Eclipse by adding it as a library
in the project properties, and then moving it "up" to the front. Didn't seem
to do it.

>>   * I tried taking the same built .jar file and putting into the jre spec
in Eclipse, at the top, and that didn't do the trick either

>>

>>

>> I've posted to newsgroups and emailed friends and still have not found the
problem.

>>

>> [Bootclasspath to the rescue?
](<http://www.javageeks.com/Papers/BootClasspath/index.htmlath/index.html>)From
reading around, I have a new angle. It would seem from the above article that
in fact, java does not look for the system class jar (rt.jar) where you would
expect it to. In fact it looks for it (on Windows) in c:Program
FilesjavaJ2SDK1.4 etc. Secondly it looks like before any other class path is
searched, the Bootclasspath picks up rt.jar and that is probably why my
previous attempts at diagnosis have failed.

>>

>> Java -X command lists some additional switches to the Sun Java VM,
including -Xbootclasspath/p: which that allows you to pre-pend a directory or
jar to the bootclasspath.


