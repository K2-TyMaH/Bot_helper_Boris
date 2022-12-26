from __future__ import annotations
from user_funcs import handler, EXIT_COMMANDS, exit_func
from address_book import address_book
from boris import boris, dobriy_den

def main():
    """
   The user enters through a space:
        - a command for the bot;
        - command, contact name, phone number or date of birth, email address, notes, tags,
    The function returns the bot's response and prints them.
    The bot terminates after the words "good bye", "exit", "close", "quit", "bye"
    """
    try: 
        
        dobriy_den()
        
        boris()
        
        # print("")
        # print("\033[1m\033[34m{}\033[0m".format("Hello, I am Bot-contacts:)"))
        # print("")
        # help_str = "\033[34m{}\033[0m".format("help")
        # print(f"Type {help_str} to see all commands")
        
        # while True:
        #     print("")
        #     input_string = input("Input command, please: ")
        #     if input_string.lower() in EXIT_COMMANDS:
        #         exit_func()
        #     get_command = handler(input_string)
        #     print(get_command)
    
    except Exception:
        print("\nAn unexpected error has occurred...")
        main()        

    finally:
        address_book.save_address_book()           


if __name__ == '__main__':
    main()