
from ui.display import clear_screen, print_colored, print_banner
from core.discord_rce import connect_to_discord
import time

def show_help():
    clear_screen()
    print_colored("--- Rafef Discord RCE Help ---", "95")
    print_colored("This tool simulates an RCE exploit for Discord desktop client.", "92")
    print_colored("Please ensure Discord client is running before connecting.", "92")
    print_colored("\nOptions:", "95")
    print_colored("  1 - Connecting To Discord Client: Initiates a simulated connection.", "94")
    print_colored("  2 - Show Help: Displays this help message.", "94")
    print_colored("  3 - Exit: Exits the application.", "94")
    print_colored("\nOnce connected, you can type commands at the \'cmd >\' prompt.", "92")
    print_colored("Type \'exit\' to return to the main menu or \'log\' to view command history.", "92")
    print_colored("------------------------------", "95")
    input("Press Enter to return to main menu...")
    main_menu()

def main_menu():
    clear_screen()
    print_banner()
    print_colored("Welcome to Rafef Discord RCE!", "93") # Yellow
    print("\n")
    print_colored("1 - Connecting To Discord Client", "94") # Blue
    print_colored("2 - Show Help", "94") # Blue
    print_colored("3 - Exit", "94") # Blue
    print("\n")
    
    while True:
        print_colored("- Chose > ", "95") # Pink
        choice = input()
        if choice == "1":
            connect_to_discord()
            break
        elif choice == "2":
            show_help()
            break
        elif choice == "3":
            print_colored("Exiting Rafef Discord RCE. Goodbye!", "95")
            time.sleep(1)
            clear_screen()
            exit()
        else:
            print_colored("Error: Invalid choice. Please enter 1, 2, or 3.", "91") # Red
            time.sleep(2)
            clear_screen()
            print_banner()
            print_colored("Welcome to Rafef Discord RCE!", "93")
            print("\n")
            print_colored("1 - Connecting To Discord Client", "94")
            print_colored("2 - Show Help", "94")
            print_colored("3 - Exit", "94")
            print("\n")

if __name__ == "__main__":
    main_menu()


