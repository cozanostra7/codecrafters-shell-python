import sys
import shutil,subprocess, os


def main():
    while True:
        sys.stdout.write("$ ")
    
        command = input()
        if command == "exit":
            break
        elif command.startswith("echo "):
            print(command[5:])
        elif command.startswith("type "):
            cmd = command[5:]
            if cmd in ["echo", "exit", "type", "pwd"]:
                print(f"{cmd} is a shell builtin")
            elif path := shutil.which(cmd):
                print(f"{cmd} is {path}")
            elif command == "pwd" or command.startswith("pwd "):
                print(os.getcwd())
            else:
                print(f"{cmd}: not found")
        else:
            parts = command.split()
            if not parts:
                continue
            prog, *args = parts
            if shutil.which(prog):
                subprocess.run([prog, *args])
            else:
                print(f"{command}: command not found")

        
if __name__ == "__main__":
    main()
