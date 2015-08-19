# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > ####Most Useful Commands:####
1. **pwd** - print working directory (where you currently are)  
2. **mkdir [name]** - make directory (folder) in current directory  
  *Hint: use `mkdir -p [name/name2/etc.]` to create multiple directories simultaneously*  
3. **cd [name/name2/etc.]** - change directory (current location)  
  *Hint: only take you to directories below your current one  
  To move back up use `cd ..` (for one level up) or `cd ../../[etc.]` for more than one*  
4. **ls** - see below
5. **touch [filename.extension]** - create new empty file with name [filename.extension]  
6. **cp [copyThis] [toThis]** - copy [copyThis] file or directory to [toThis] file or directory  
  *Hint: use `cp -r [copyDir] [toDir]` to copy directories with their files*  
7. **mv [moveFrom] [moveTo]** - move a file or directory; if [moveTo] does not exist, file is simply renamed  
8. **rm [file]** - delete [file]  
  _Hint: use `rm [file1] [file2] [etc.]` to delete multiple files;  
  use `rm -r [directory]` to delete a directory and its sub-directories;  
  use `rm -rf [directory]` to delete a directory and all its contents;  
  use `rm -rf *` to delete all directories and files in the current location_  
9. **$ | $** - the | takes the output from the command on the left, and "pipes" it to the command on the right  
10. **$ < $** - the < will take and send the input from the file on the right to the program on the left  
11. **$ > $** - the > takes the output of the command on the left, then writes it to the file on the right  
12. **$ >> $** - the >> takes the output of the command on the left, then appends it to the file on the right  
13. __*__ - use the * (asterisk) symbol to say "anything." 
14. **xargs** - see below
15. **find [startDir] -name [wildcard] -print** - find files  
  *Hint: use `.` for [startDir] to start in the current directory*  
16. **grep [string] [file]** - search for [string] inside [file]  
  _Hint: use `grep -i [string] [file]` to ignore [string] case;  
  use "\*", "\*.txt", etc. to make your search more powerful_  
17. **echo [something]** - print [something]  
  *Hint: use `echo $[variable]` as [something] to reference a stored variable*  
18. **export [variable]=[value]** - set/modify an environment [variable] equal to [value]  
19. **unset [variable]** - delete / unset [variable]

---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

> > **ls [name]** - lists contents of [name] directory; if no directory specified, uses current location  
  - *Hint: `ls -lR` recursively lists all contents, sub-contents, etc.*  
  - *Hint: `ls -a` all contents including hidden files*    
  - *Hint: `ls -l` lists all contents with greater detail (in addition to name also shows file size, modified date, owner / group, permissions, etc.)*  
  - *Hint: `ls -lh` does the same thing but shows the file sizes in a more human friendly way*  
  - *Note: all combinations of the above flags are meaningful*  

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

