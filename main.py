import sys
from FileManager import FileManager
from ux_functions import clear_cli,in_bold
from file_manager import check_files,create_database
from helper_functions import welcome_message,menu


def main():
    myfilemanager = FileManager()
    clear_cli()
    welcome_message()
    while True:
        menu()
        try:
            user_say = input(in_bold("Type selection here: "))
            while user_say not in ["1", "2", "3", "4"]:
                user_say = input(in_bold(
                    "Invalid choice.\n"
                    "Type selection between 1 and 4: "))
        except (EOFError, KeyboardInterrupt):
            clear_cli()
            sys.exit(in_bold("\nThank you for using LabTrack!\n"))

        if user_say == "1":
            print(myfilemanager.filepath)
            check_files(myfilemanager)
            print(myfilemanager.filepath)
            # TODO get path, valid pdf to use in other options
        elif user_say == "2":
            create_database(myfilemanager.filepath)
        elif user_say == "3":
            print("three")
        elif user_say == "4":
            print("exit")
            clear_cli()
            sys.exit(in_bold("\nThank you for using LabTrack!\n"))



if __name__ == "__main__":
    main()


# TODO EOFError and KeyboardInterrupt repeats a lot. How to handle in one place?
    # Also more user friendly approach be to double check if want to exit, now terminates.
