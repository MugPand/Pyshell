# Pyshell

Pyshell is a Unix Shell developed fully in Python to replicate an assignment from Princeton COS 217 - Spring 2020. I decided to develop my own shell in Python to expand my knowledge of file structures and to increase my familiarity with Python. More information on the original assignment (creating a Unix Shell in C) can be found at https://www.cs.princeton.edu/courses/archive/spring20/cos217/asgts/07shell/.

## Getting Started

To get started:

1. Run ```pip install -r requirements.txt```
1. Start the shell by running ``` python main.py ```

## Usage

The shell takes many user commands, flags, and arguments as outlined below.

Commands Available:

- ```"quit"``` or ```"exit"```: quits the shell,
- ```"status"```: prints status of shell i.e. running or aborted,
- ```"path"```: prints directory path, add tag ```-f``` or ```-d``` for file or directory path respectively,
- ```"log"```: prints log of every shell command entered,
- ```"clog" x```: clears x number of entries in log ,
- ```"mkdir" x```: creates a directory x with the specified name, add tag ```-t``` to make temporary directory
- ```"rmdir" x```: removes a directory x with the specified name
- ```"ls"```: lists current directory,
- ```"cd" x```: changes current directory to the specified one x
- ```"help"```: displays general help menu
- ```"clr" PATH=x FILE=y DIR=z```: changes color profile of shell with specifiedattributes
                   From Colorama, Available Formatting Constants are: ```BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET```