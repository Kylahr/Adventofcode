import os

def create_sequential_folder():
    # Get the list of folders in the current directory
    folders = [f for f in os.listdir() if os.path.isdir(f) and f.isdigit()]
    
    # Find the next folder name
    if folders:
        # Sort folder names as integers and get the last one
        folders.sort(key=lambda x: int(x))
        last_folder = int(folders[-1])
        new_folder_name = f"{last_folder + 1:02}"
    else:
        # Start from 01 if no folder exists
        new_folder_name = "01"
    
    # Create the new folder
    os.mkdir(new_folder_name)
    print(f"Folder '{new_folder_name}' created.")

    # Define file names
    file_1 = os.path.join(new_folder_name, f"day_{new_folder_name}_1.py")
    file_2 = os.path.join(new_folder_name, f"day_{new_folder_name}_2.py")
    file_3 = os.path.join(new_folder_name, f"day_{new_folder_name}.txt")

    # Create files in the new folder
    open(file_1, 'w').close()
    open(file_2, 'w').close()
    open(file_3, 'w').close()
    print(f"Files '{file_1}', '{file_2}', and '{file_3}' created.")

# Run the function
if __name__ == "__main__":
    create_sequential_folder()