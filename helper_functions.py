from Manager import UXManager

def welcome_message():
    print(UXManager.in_bold("Welcome to LabTrack"))
    print("Your personal assistant to track your blood test results.\n")

def menu():
    print(UXManager.in_bold("LabTrack is here to help you:"))

    # Create a dict, key == str & value == str
    menu_options = {
        "1": "Upload your lab. test files",
        "2": "Track specific details",
        "3": "Prepare results for sharing",
        "4": "Exit"
    }

    for key, value in menu_options.items():
        print(f"{UXManager.in_bold('[' + key + ']')} {value}")