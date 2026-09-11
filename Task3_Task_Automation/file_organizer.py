import os
import shutil
def display_header():
    print("\n"+"="*60)
    print("             JPG FILE ORGANIZER")
    print("="*60)
def get_folder_path():
    while True:
        folder=input("Enter the folder path to organize: ").strip()
        if not os.path.exists(folder):
            print("Folder does not exist. Please enter a valid path.")
        elif not os.path.isdir(folder):
            print("The given path is not a folder.")
        else:
            return folder
def find_jpg_files(folder):
    jpg_files=[]
    for file in os.listdir(folder):
        file_path=os.path.join(folder,file)
        if os.path.isfile(file_path) and file.lower().endswith((".jpg",".jpeg")):
            jpg_files.append(file)
    return jpg_files
def organize_files(folder,jpg_files):
    if not jpg_files:
        print("\nNo JPG or JPEG files found in the selected folder.")
        return 0
    destination=os.path.join(folder,"JPG_Files")
    os.makedirs(destination,exist_ok=True)
    moved_count=0
    for file in jpg_files:
        source=os.path.join(folder,file)
        target=os.path.join(destination,file)
        if os.path.exists(target):
            base,extension=os.path.splitext(file)
            counter=1
            while os.path.exists(target):
                new_name=f"{base}_{counter}{extension}"
                target=os.path.join(destination,new_name)
                counter+=1
        try:
            shutil.move(source,target)
            print(f"Moved: {file}")
            moved_count+=1
        except Exception as error:
            print(f"Could not move {file}: {error}")
    return moved_count
def show_summary(folder,moved_count):
    print("\n"+"-"*60)
    print("              ORGANIZATION SUMMARY")
    print("-"*60)
    print("Source Folder :",folder)
    print("Files Moved   :",moved_count)
    if moved_count>0:
        print("Destination    :",os.path.join(folder,"JPG_Files"))
        print("Status         : Successfully Organized")
    else:
        print("Status         : No files were moved")
    print("-"*60)
def main():
    display_header()
    print("This program automatically moves JPG/JPEG files")
    print("from a selected folder into a separate JPG_Files folder.\n")
    folder=get_folder_path()
    jpg_files=find_jpg_files(folder)
    print(f"\nJPG/JPEG files found: {len(jpg_files)}")
    if jpg_files:
        print("\nFiles to be organized:")
        for file in jpg_files:
            print(" -",file)
    confirmation=input("\nDo you want to organize these files? (y/n): ").lower().strip()
    if confirmation=="y":
        moved_count=organize_files(folder,jpg_files)
        show_summary(folder,moved_count)
    else:
        print("\nOperation cancelled. No files were moved.")
    print("\nThank you for using JPG File Organizer!")
if __name__=="__main__":
    main()
