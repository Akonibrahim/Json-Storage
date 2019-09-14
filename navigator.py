import os
from JsonParser import JsonParser
class Navigator():
    
    def __init__(self):
        current_directory = os.getcwd()
        print("\n")
        print(f"Current Directory : \t {current_directory}")
        current_files = self.show_json_files_here()
        print("\n")
        value = eval(input("Choose a folder or JSON file :"))
        if isinstance(value,int):
            if value == 0:
                splittedversion = current_directory.split("/")
                if(len(splittedversion) > 2):
                    splittedversion.pop()
                    changed_dir = ("/").join(splittedversion)
                    os.chdir(changed_dir)
                    Navigator()
                else:
                    print("\n","<<<<< You are at the root >>>>>>")
                    Navigator()
            elif value == 1:
                JsonParser(current_directory)
                
            elif value in range(len(current_files)+1):
                if(current_files[value].endswith(".json")):
                    JsonParser(current_directory+"/"+current_files[value])
                else:
                    os.chdir(current_directory+"/"+current_files[value])
                    Navigator()

                print(f'current_directory ====== {current_directory+"/"+current_files[value]}')
                Navigator()
            else:
                print("\n","<<<<< Please enter a valid option >>>>>>")
                Navigator()    

        else:
            print("\n","<<<<< Please enter a valid option >>>>>>")
            Navigator()

        
    def show_json_files_here(self):
        
        files_here = os.listdir()
        folders , json_files  = ["<< GO BACK >> ","<< To create a file here >>"] , []

        if len(files_here) > 0:
            
            for files in files_here:
                splitted_file_name = files.split(".")
                if len(splitted_file_name) > 1:
                    if splitted_file_name[-1] == "json":
                        json_files.append(files)
                else:
                    folders.append(files)
            total = folders + json_files
            print('------------------------------------------------')
            print('\tFolders and Jsonfiles here')
            print('------------------------------------------------')
            if (len(total) > 0):
                for idx,folder in enumerate(total):
                    print (f"\t{idx}. {folder} \t")
                return total
            else:
                print("\tNo folders or file in this directory")
        else:
            print("Empty directory!")

if __name__ == "__main__":
    json_obj = Navigator()