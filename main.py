import sys
from FileManager import FileManager
from ux_functions import clear_screen,in_bold
from file_manager import get_filepath,create_database
from helper_functions import welcome_message,menu,quit_program
from export_functions import export_to_csv


def main():
    myfilemanager = FileManager()
    clear_screen()
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
            quit_program

        if user_say == "1":
            get_filepath(myfilemanager)
            # TODO get path, valid pdf to use in other options
        elif user_say == "2":
            # create a database and put it into database.json
            create_database(myfilemanager.filepath)
        elif user_say == "3":
            export_to_csv()
        elif user_say == "4":
            quit_program



if __name__ == "__main__":
    main()


# TODO EOFError and KeyboardInterrupt repeats a lot. How to handle in one place?
    # Also more user friendly approach be to double check if want to exit, now terminates.
