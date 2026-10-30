import sys
import shutil


def main():
    while True:
        sys.stdout.write("$ ")
    
        command = input()
        if command =='exit':
                    break
        elif command[5:] in ["type", "echo", "exit"]:
            print(f"{command[5:]} is a shell builtin")
        elif path := shutil.which(command):
             print(f"{command} is {path}")
        
        elif command.startswith('echo'):
              print(command[5:])


        else:
            print(f"{command.strip('type ')}: not found")

        
if __name__ == "__main__":
    main()
