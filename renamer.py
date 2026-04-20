import os

# 1. SMART PATH LOCATOR 
# This finds your folder even if it is hidden inside OneDrive
user_path = os.environ['USERPROFILE']
paths_to_check = [
    os.path.join(user_path, 'OneDrive', 'Desktop', 'TestFiles'),
    os.path.join(user_path, 'Desktop', 'TestFiles')
]

folder_path = ""
for path in paths_to_check:
    if os.path.exists(path):
        folder_path = path
        break

# 2. THE LOGIC
if folder_path == "":
    print("---------------------------------------------------------")
    print("ERROR: I still can't find 'TestFiles' on your Desktop.")
    print("Please make sure the folder is named exactly 'TestFiles'.")
    print("---------------------------------------------------------")
else:
    # Ask for the new name
    new_prefix = input("Enter the new name for your files: ")
    
    # Get all files inside that folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    if len(files) == 0:
        print("The folder is empty! Put some files in 'TestFiles' first.")
    else:
        print(f"Found {len(files)} files. Starting rename...")

        for index, filename in enumerate(files):
            # Keep the original file extension (.jpg, .png, etc.)
            file_ext = os.path.splitext(filename)[1]
            
            # Create the new name (e.g., MyProject_1.jpg)
            new_name = f"{new_prefix}_{index + 1}{file_ext}"
            
            source = os.path.join(folder_path, filename)
            destination = os.path.join(folder_path, new_name)
            
            # Rename the file
            os.rename(source, destination)
            print(f"Renamed: {filename} -> {new_name}")

        print("---------------------------------------------------------")
        print("SUCCESS! Check your TestFiles folder on the Desktop.")
        print("---------------------------------------------------------")