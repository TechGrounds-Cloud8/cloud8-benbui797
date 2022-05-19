# LNX-03 Working with text (CLI)
Learning to do common text operations using Linux CLI.

## Key terminology
- echo (print to terminal)
- echo text > filename (print to file)
- echo text >> filename (append newline to file)
- cat textfile (prints contents of textfile to terminal)
- grep -> "global regular expression print" (use this to filter partial text)
- regular expressions (code to describe language patterns)

### Redirections
redirections of 1-stdin, 2-stdout, 3-stderr
- `>` = redirect stdout in write mode
- `>>` = redirect stdout in append mode
- `2>` = redirect stderr in write mode
- `2>>` = redirect stderr in append mode
- `|`  = redirect output of program1 to input of program2

### grep additional arguments:
- -i (make regex case insensitive)
- grep -A (command is used to display the line after the result.)
- grep -B (command is used to display the line before the result.)
- grep -C (command is used to display the line after and line before the result.)

## Exercise
### Sources
- https://www.w3cschoool.com/linux-grep  
- I was already familiar with some of the commands
- https://www.putorius.net/linux-io-file-descriptors-and-redirection.html

### Overcome challenges
- N/A

### Results
![LNX-03 screenshot](../00_includes/LNX-03.png)
