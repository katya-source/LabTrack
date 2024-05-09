import sys,json,re,os
import FileManager
from pdfminer.high_level import extract_text
from ux_functions import clear_screen,in_bold
from helper_functions import quit_program

def get_filepath(myfilemanager):
    while True:
        clear_screen()
        print(in_bold("[ Upload your lab. test files ]\n"))

        try:
            myfilemanager.filepath = input("Enter path: ")
            is_valid = myfilemanager.is_valid_path()

            if is_valid:
                print(f"Result after uploading files: {myfilemanager.filepath}")
                # TODO different return, need to standartize for usage later?
                # If path and valid returned then proceed, else print details missing
                return

            print('Try again')
            print('Go back to main menu')

            user_say = input(in_bold("Type selection here: "))

            while user_say not in ["1", "2"]:
                user_say = input(in_bold(
                    "Invalid choice.\n"
                    "Type selection between 1 and 2: "))

            if user_say == "1":
                continue

            clear_screen()
            return

        except (EOFError, KeyboardInterrupt):
            quit_program


    # print('\n')
    upload_files_options = {
        # "1": "Enter path again",
        # "2": "Back",
    }

    # for key, value in upload_files_options.items():
    #     print(f"{in_bold('[' + key + ']')} {value}")

# def access_pdf():
#     try:
#         path = input("Enter path: ")
#         return path
#     except (EOFError, KeyboardInterrupt):
#         clear_screen()
#         sys.exit(in_bold("\nThank you for using LabTrack!\n"))


def create_database(pdf_dir):
    data_from_pdf = {}
    raw_data = {}
    
    # Loops over each file in the directory
    for filename in os.listdir(pdf_dir):
        # Checks if the file is a PDF
        if filename.endswith('.pdf'):
            # Reads the text from the PDF
            text = extract_text(os.path.join(pdf_dir, filename))
            raw_data[filename] = text
            if "E. sveikatos portalas" in text:
                # Extracts the specific details from the text
                details = extract_data(text)
                data_from_pdf[filename] = details
            else:
                data_from_pdf[filename] = None
    with open('database.json', 'w') as file:
        json.dump(data_from_pdf, file, indent=4)
    with open('rawData.json', 'w') as file:
        json.dump(raw_data, file, indent=4)


def extract_data(text):
# TODO understand if nested dicts are better than list of dicts
    pattern_data = {
            "Report date & time": r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2})',
            "Hemoglobin result": r'(HGB|HB)[\s\S]*?(\d+)'
        }

    pattern_levels = r'(\d+[\.\d{0,2}]*)\s*(?:-|–|iki)\s*(\d+[\.\d{0,2}]*)'
    # r'\[?(\d+[\.\d{0,2}]*)\s*(?:-|–|iki)\s*(\d+[\.\d{0,2}]*)\]?'
    pattern_date = r'(\d{4}[-.]\d{2}[-.]\d{2})'

    extracted_data = {}
    for detail, pattern in pattern_data.items():
        match = re.search(pattern, text)
        if match is not None:
            # If the pattern is found, store the matched string in the dictionary
            if detail == "Hemoglobin result":
                hemoglobin_data = {}  #
                hemoglobin_data["result"] = match.group(2)  #
                # extracted_data[detail] = match.group(2)  #
                # Search for levels after the result
                match_levels = re.search(pattern_levels, text[match.end():])
                if match_levels is not None:
                    hemoglobin_data["levels from lab."] = match_levels.group().replace('iki', '-')  #
                    # extracted_data["Hemoglobin levels from lab."] = match_levels.group().replace('iki', '-') #
                else:
                    hemoglobin_data["levels from lab."] = "Levels not found"  #
                    # extracted_data["Hemoglobin levels from lab."] = "Levels not found"  #
                match_date = re.findall(pattern_date, text[:match.start()])
                if match_date:
                    hemoglobin_data["analysed on"] = match_date[-1]  #
                    # extracted_data["Hemoglobin analysed on"] = match_date[-1]  #
                else:
                    hemoglobin_data["analysed on"] = "Date not found"  #
                extracted_data["Hemoglobin"] = hemoglobin_data  #
                    # extracted_data["Hemoglobin analysed on"] = "Date not found"  #
            else:
                extracted_data[detail] = match.group()
        else:
            # If the pattern is not found, store an empty string in the dictionary
            extracted_data[detail] = ""
    return extracted_data