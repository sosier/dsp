# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > REPLACE THIS TEXT WITH YOUR RESPONSE

---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

> > REPLACE THIS TEXT WITH YOUR RESPONSE

---


---

What does `xargs` do? Give an example of how to use it.

> > **xargs** - when used in combination with `$ | $`, executes arguments that `$ | $` would not be able to do alone  
  - *Hint: `xargs` alone opens a prompt for you to enter text, which it then `echo`es; in this way, `xargs` can be used to customize how results are output*  
  - *For example: `ls | xargs -n 1` lists the contents of your current directory with one item on each line instead of a big, hard to read mass of files, folders, etc.*  
  - *Another common use of `xargs` is in conjunction with `find`*  
  - _For example: `find . -name "*.txt" -print | xargs rm` would perform a search for all .txt files and remove them in one command_  
  - _Note: `find . -name "*.txt" -print | rm` would fail_  

---

