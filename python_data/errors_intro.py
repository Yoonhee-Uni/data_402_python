# try:
#     file = open("order.txt")
#     file_lines = file.readlines()
#     print(file_lines)
#
# except FileExistsError as msg:
#     print("error error errrrrror")
#     print(msg)
# finally:
#     file.close()
#     print("Execution complete")
#
def reading_files(file):
    try:
        with open(file, "r")as file:
            file_lines = file.readlines()
            return file_lines
    except FileNotFoundError:
        print("error")
    finally:
        print("Execution complete")

new_file = reading_files("order.txt")
print(new_file)


def write_to_file(order_item, file="order.txt"):
    try:
        with open(file, "a") as file:
            file.write('\n' + order_item)
    except:
        print("file not found")
write_to_file("milk")
print(reading_files())