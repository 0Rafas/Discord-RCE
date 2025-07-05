
import time
import os
from ui.display import print_colored, clear_screen, show_loading

command_log = []
current_working_directory = "/home/discord_server"

def connect_to_discord():
    show_loading("Connecting Loading...", "91") # Red
    
    # Simulate connection delay
    time.sleep(2) 
    
    clear_screen()
    print_colored("Accepted Connection", "95") # Pink
    print_colored("Enter commands to execute on the Discord server (type \'exit\' to quit, \'log\' to view command log, \'help_cmd\' for command help):", "91") # Red
    while True:
        command = input(f"\033[94mcmd {current_working_directory}> \033[0m") # Blue
        if command.lower() == "exit":
            break
        elif command.lower() == "log":
            view_command_log()
        elif command.lower() == "help_cmd":
            show_command_help()
        else:
            execute_command(command)

def execute_command(command):
    global current_working_directory
    command_parts = command.split(" ", 1)
    cmd = command_parts[0].lower()
    args = command_parts[1] if len(command_parts) > 1 else ""

    output = ""
    error = False

    if cmd == "ls":
        output = "file1.txt\nfile2.py\nfolder_a\nfolder_b"
    elif cmd == "pwd":
        output = current_working_directory
    elif cmd == "whoami":
        output = "discord_admin"
    elif cmd == "echo":
        output = args
    elif cmd == "cd":
        if args == "..":
            parent_dir = os.path.dirname(current_working_directory)
            if parent_dir != "/": # Prevent going above root
                current_working_directory = parent_dir
            else:
                current_working_directory = "/"
            output = f"Changed directory to {current_working_directory}"
        elif args.startswith("/"):
            current_working_directory = args
            output = f"Changed directory to {current_working_directory}"
        elif args:
            new_path = os.path.join(current_working_directory, args)
            current_working_directory = new_path
            output = f"Changed directory to {current_working_directory}"
        else:
            output = "Usage: cd <directory>"
            error = True
    elif cmd == "systeminfo":
        output = "OS Name: Discord Server OS\nOS Version: 1.0.0\nSystem Type: x64-based PC\nTotal Physical Memory: 16,384 MB"
    elif cmd == "clear_log":
        global command_log
        command_log = []
        output = "Command log cleared."
    else:
        output = f"Error: Command not found: {cmd}"
        error = True

    if error:
        print_colored(output, "91") # Red for errors
    else:
        print(output)
    print("Command executed successfully (simulated).")
    command_log.append(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - {command} -> {"Error" if error else "Success"}')

def view_command_log():
    clear_screen()
    print_colored("--- Command Log ---", "95")
    if not command_log:
        print_colored("No commands executed yet.", "93") # Yellow
    else:
        for entry in command_log:
            print_colored(entry, "92") # Green
    print_colored("-------------------", "95")
    input("Press Enter to continue...")
    clear_screen()
    print_colored("Accepted Connection", "95") # Pink
    print_colored("Enter commands to execute on the Discord server (type \'exit\' to quit, \'log\' to view command log, \'help_cmd\' for command help):", "91") # Red

def show_command_help():
    clear_screen()
    print_colored("--- Available Commands (Simulated) ---", "95")
    print_colored("ls: List directory contents.", "94")
    print_colored("pwd: Print name of current working directory.", "94")
    print_colored("whoami: Print effective userid.", "94")
    print_colored("echo <text>: Display a line of text.", "94")
    print_colored("cd <directory>: Change the current working directory.", "94")
    print_colored("systeminfo: Display system information.", "94")
    print_colored("clear_log: Clear the command history log.", "94")
    print_colored("exit: Return to the main menu.", "94")
    print_colored("log: View the command history log.", "94")
    print_colored("--------------------------------------", "95")
    input("Press Enter to continue...")
    clear_screen()
    print_colored("Accepted Connection", "95") # Pink
    print_colored("Enter commands to execute on the Discord server (type \'exit\' to quit, \'log\' to view command log, \'help_cmd\' for command help):", "91") # Red


