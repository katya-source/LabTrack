import csv
import json

def export_to_csv():
    # print instruction
    # ask user for file name
    # check if filename is with csv extension
    file_name = 'test.csv'
    # write database.json to csv

    db_dict = read_into_dict('database.json')

    with open(file_name, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['Date','Result'],delimiter=';')
        writer.writeheader()
        writer.writerow(db_dict)


    # print success message
    pass

def read_into_dict(file_name):
    with open(file_name, 'r') as f:
        data = json.load(f)
    return data