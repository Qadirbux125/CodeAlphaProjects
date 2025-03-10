import os
import shutil

# Define the directory to organize
directory_to_organize = "D:\Automating File Organization file example"  # Replace with your directory path

# Define file types and their corresponding folders
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".sh", ".js", ".html", ".css"],
    "Others": []  # For files that don't match any category
}

def create_folders():
    """Create folders for each file type if they don't already exist."""
    for folder_name in file_types.keys():
        folder_path = os.path.join(directory_to_organize, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created folder: {folder_name}")

def organize_files():
    """Move files into their respective folders based on their extensions."""
    for filename in os.listdir(directory_to_organize):
        file_path = os.path.join(directory_to_organize, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get the file extension
        _, file_extension = os.path.splitext(filename)
        file_extension = file_extension.lower()

        # Find the appropriate folder for the file
        moved = False
        for folder_name, extensions in file_types.items():
            if file_extension in extensions:
                destination_folder = os.path.join(directory_to_organize, folder_name)
                shutil.move(file_path, destination_folder)
                print(f"Moved {filename} to {folder_name}")
                moved = True
                break

        # If the file type is not recognized, move it to the "Others" folder
        if not moved:
            destination_folder = os.path.join(directory_to_organize, "Others")
            shutil.move(file_path, destination_folder)
            print(f"Moved {filename} to Others")

if __name__ == "__main__":
    print("Starting file organization...")
    create_folders()
    organize_files()
    print("File organization complete!")