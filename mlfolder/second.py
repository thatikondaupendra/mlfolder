import os
import sys
class NirnayOSClass:
    def _init_(self):
        pass
    def print_current_working_directory(self):
        cwd=os.getcwd()
        print("The present working directory is{}".format(cwd))
    def changed_current_working_directory(self,path_to_new_dir):
        cwd=os.getcwd()
        return_code=os.chdir(path_to_new_dir)
        print("directory changed from {} to {}:".format(cwd,path_to_new_dir))
    def listd(self,dir_path_to_list):
        dir_path_to_list=os.getcwd()
        list_of_contents=os.listdir(dir_path_to_list)
        print("The contents in the current directory are::")
        for file_or_folder_name in list_of_contents:
            print(file_or_folder_name,end="\t")
        print()
def main():
    while(True):
        print("please choose one of the appropriate options::")
        print("1.To check the current directory of the code execution.(using the getcwd() function)")
        menu_choice=input()
        menu_choice=int(menu_choice)
        dir_entity=NirnayOSClass()
        if menu_choice==1:
            dir_entity.print_current_working_directory()
        elif menu_choice==2:
            print(">enter the absolute path to the nuew directory to which w want to change::")
            input_str=input()
            dir_entity.changed_current_working_directory(input_str)
if __name__=='__main__':
    main()
