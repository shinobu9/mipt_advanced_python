import zipfile
import os

flag = True
while flag:
    zip_name = input("Enter zip: ")
    try:
        with zipfile.ZipFile(zip_name, 'r') as zip_ref:
            dir_name = zip_name[:-4] #"C:/Users/kamelis/Desktop/main"
            zip_ref.extractall(dir_name)
            flag = False
            print("File extracted into", dir_name)
    except FileNotFoundError:
        print("Bad zip path, try again")
    except Exception:
        print("Unknown interrupt")

answer_list = []

for current_dir, dirs, files in os.walk(dir_name):
    for file in files:
        if ".py" in file:
            #answer.write(current_dir)
            #answer.write('\n')
            answer_list.append(current_dir)
            break


answer_list.sort()

flag = True
while flag:
    ans_path = input("Enter answer file: ")
    try:
        answer = open(ans_path, "w")
        for line in answer_list:
            answer.write(line)
            answer.write('\n')
        answer.close()
        flag = False
        print("Answer written successfully")
    except FileNotFoundError:
        print('No such directory, try again')
    except Exception:
        print("Unknown interrupt")

        