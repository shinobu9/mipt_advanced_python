flag = True
while flag:
    file_name = input("Enter file: ")
    try:
        with open(file_name, "r") as file:
            for line in file:
                print(line.strip())
        flag = False
    except FileNotFoundError:
        print("Bad file path, try again")
        
list_of_lines = ['for both', 'of oars',
                 'with little skill',
                 'by little arms',
                 'are plied']

def write_array(arr, file_name):
    with open(file_name, "w") as f:
        for line in arr:
            f.write(line)
            f.write('\n')
            
flag = True
while flag:
    new_file = input("Enter file to write lines: ")
    try:
        write_array(list_of_lines, new_file)
        flag = False
        print("Success")
    except FileNotFoundError:
        print("Directory does not exist, try again")