import csv
#
# with open("user_details.csv", newline='') as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=",")
#     print(csvreader)
#     for row in csvreader:
#         print(row)
#
# with open("user_details.csv", newline='') as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=",")
#     csv_list = list(csvreader)
#
# with open("new_user_details", "w") as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerows(csv_list)
#
# print("this",csv_list)

#Assignment
#transform csv_list into transformed_list
# [firstname, lastname, email]
#include tests
# include functiones and try/except


def read_file(file):
    try:
        with open(file) as csvfile:
            csvreader = csv.DictReader(csvfile)
            csv_list =[]
            for row in csvreader:
                csv_list.append([row['firstName'], row['lastName'], row['email']])
        return csv_list
    except FileNotFoundError:
        print("Can't find file")





