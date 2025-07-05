
import os
import time

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def print_colored(text, color_code, end="\n"):
    if os.name == "nt": # Check if running on Windows
        print(text, end=end) # Print without color codes on Windows
    else:
        print(f"\033[{color_code}m{text}\033[0m", end=end)

def print_banner():
    print_colored("██████╗  █████╗ ███████╗███████╗ ██████╗ ██████╗ ███████╗", "95") # Pink
    print_colored("██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝ ██╔══██╗██╔════╝", "95") # Pink
    print_colored("██████╔╝███████║███████╗███████╗██║  ███╗██████╔╝█████╗  ", "95") # Pink
    print_colored("██╔══██╗██╔══██║╚════██║╚════██║██║   ██║██╔══██╗██╔══╝   ", "95") # Pink
    print_colored("██║  ██║██║  ██║███████║███████║╚██████╔╝██║  ██║███████╗", "95") # Pink
    print_colored("╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝", "95") # Pink
    print_colored("                                                         DisRCE", "95") # Pink
    print("\n")

def show_loading(message, color_code):
    clear_screen()
    print_colored(message, color_code)
    for i in range(10):
        if os.name == "nt":
            print("." * (i % 4))
        else:
            print_colored("." * (i % 4), color_code)
        time.sleep(0.5)
        clear_screen()
        print_colored(message, color_code)



