from pathlib import Path
import logging, os, tempfile, colorama

# imports colorama functions for changing text styles/colors
from colorama import Fore, Style, Back, init


# status defines if the shell is running
status = True

# list of commands for logger to read
command_list = []

# creates logger
logger = logging.getLogger('log_history')
logger.setLevel(logging.DEBUG)

# creates console handler and sets its level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# creates formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# adds formatter to ch
ch.setFormatter(formatter)

# adds ch to logger
logger.addHandler(ch)

# resets color profile
init(autoreset=True)
pathColor = Fore.MAGENTA
fileColor = Fore.GREEN
dirColor = Fore.BLUE

# number of argument checker
def arg_checker(num_of_tokens, num_of_args):
    if num_of_tokens > num_of_args:
        print("Invalid number of arguments")
        return False
    elif num_of_tokens != num_of_args:
        print("Invalid number of arguments")
        return False
    return True
    
    
# COMMAND DEFINITIONS

# quit function that safely exits the shell
def  quit():
    global status
    status = False
    print("Pyshell exited")

# prints out the current status of the shell
def status():
    if status:
        print("status: running")
    else:
        print("status: aborted")
    command_list.append("status")

# path function that prints out the file path or directory path. -f or -d flags can be addded to specify file and directory respectively. Path defaults to directory.
def path():
    if(arg_checker(len(key), 2)):
        if len(key) == 2 and key[1] == "-f":
            print("File Path= ", Path(__file__).absolute())
            command_list.append("path -f")
        elif len(key) == 1 or key[1] == "-d":
            print("Directory Path= ", Path().absolute())
            command_list.append("path -d")            
        else:
            print("Invalid Arguments Entered")
    else: return

#log function that prints out a log history of the commands entered
def log():
    for i in command_list:
        logger.info(i)
    command_list.append("log")

# default function for invalid commands
def default():
    print("Invalid command. Type help for more info. ")

# clears x number of entries in the log
def clog():
    if(len(key) == 1):
        del command_list[:]
    elif(arg_checker(int(key[1]), len(command_list))):
        for i in range(int(key[1])):
            command_list.pop()

    if len(command_list) == 0:
        print("Log cleared. ")
    else:
        print("Last " + key[1] + " logs cleared.")
    command_list.append("clog")

def mkdir():
    if(len(key) == 3 and key[2] == "-t"):
        with tempfile.TemporaryDirectory() as directory:
            print('The created temporary directory is %s' % directory)


    if(arg_checker(len(key), 2)):
        access_rights = 0o755

        try:
            os.mkdir(key[1], access_rights)
        except OSError:
            print ("Creation of the directory %s failed" % key[1])
        else:
            print ("Successfully created the directory %s" % key[1])
            command_list.append("mkdir")
    

# def rmdir():
def rmdir():
    if(arg_checker(len(key), 2)):
        try:
            os.rmdir(key[1])
        except OSError:
            print ("Deletion of the directory %s failed" % path)
        else:
            print ("Successfully deleted the directory %s" % path)
            command_list.append("rmdir")
        
def ls():
    for x in os.listdir('.'):
        if(os.path.isdir(x)):
            print(dirColor + x)
        elif(os.path.isfile(x)):
            print(fileColor + x)
        else:
            print(x)
    command_list.append("ls")

def cd():
    if(arg_checker(len(key), 2)):
        prevdir = os.getcwd()
        try:
            currPath = os.chdir(key[1])
            command_list.append("cd")
        except:
            print("/" + key[1] + " directory not found. ")
            currPath = prevdir

def clr():
    global pathColor, fileColor, dirColor
    # custom arg checker
    if(len(key) == 1):
        print("Inavlid use of command. ")
    else:
        colors = ["BLACK", "RED", "GREEN", "YELLOW", "BLUE", "MAGENTA", "CYAN", "WHITE", "RESET"]
        constants = [Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE, Fore.RESET]
        types = ["PATH", "FILE", "DIR"]
        properties = key[1:]
        for prop in properties:
            vals = prop.split("=")
            if vals[0] not in types:
                print("Invalid use of command. ")
            elif vals[1] not in colors:
                print("Invalid color argument. ")
            else:
                if vals[0] == "PATH":
                    pathColor = constants[colors.index(vals[1])]
                elif vals[0] == "FILE":
                    fileColor = constants[colors.index(vals[1])]
                elif vals[0] == "DIR":
                    dirColor = constants[colors.index(vals[1])]
                print("Color profile successfully modified. ")
                command_list.append("clr")




def help():
    if(arg_checker(len(key), 1)):
        print("""Available Commands: 
            "quit\" or \"exit\": quits the shell,
            "status\": prints status of shell i.e. running or aborted,
            "path\": prints directory path, add tag -f or -d for file or directory path respectively,
            "log\": prints log of every shell command entered,
            "clog\" x: clears x number of entries in log ,
            "mkdir\" x: creates a directory x with the specified name, add tag -t to make directory temporary
            "rmdir\" x: removes a directory x with the specified name
            "ls\": lists current directory,
            "cd\" x: changes current directory to the specified one x
            "help\": displays general help menu
            "clr\" PATH=x FILE=y DIR=z, changes color profile of shell with specified attributes
                   From Colorama, Available Formatting Constants are: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET""")
        command_list.append("help")


# main shell loop
global currPath
while status:
    currPath = os.getcwd()
    token = input(pathColor + str(currPath) + " ~$: ")
    if(token == ""):
        print("Invalid command. ")
    else:
        key = token.split()

        # commands switch block
        commands = {
            "quit": quit,
            "exit": quit,
            "status": status,
            "path": path,
            "log": log,
            "clog": clog,
            "mkdir": mkdir,
            "rmdir": rmdir,
            "ls": ls,
            "cd": cd,
            "help": help,
            "clr": clr,
            
        }
        commands.get(key[0], default)()

exit()
