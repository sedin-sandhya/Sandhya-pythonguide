# The program is basically a mini version of Windows File Explorer's 
# Sort by Type feature: it scans a folder, groups files by file type, 
# moves them into matching folders, and reports what it did.
# Organising: Downloads
# -------------------------

# Moved photo.jpg    -> Images/
# Moved resume.pdf   -> Documents/
# Moved movie.mp4    -> Videos/
# Moved archive.zip  -> Others/

# -------------------------
# Summary:
# Images: 1 files
# Documents: 1 files
# Videos: 1 files
# Others: 1 files

# Total: 4 files organised

import os
import shutil
from pathlib import Path

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Others": [] 
}

def get_category(extension):
    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category
    return "Others"

def organise_folder(folder_path: str) -> dict: 

    # scans folder, moves files, returns summary dict 
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' does not exist")
        return {}
    
    folder = Path(folder_path)

    summary = {
        "Images" : 0,
        "Documents": 0,
        "Videos": 0,
        "Others": 0
    }

    print(f"Organising: {folder_path}")
    print("*" * 20)

    for item in folder.iterdir():
        if not item.is_file():
            continue
        
        extension = item.suffix.lower()

        category = get_category(extension)

        destination_folder = folder / category
        print(destination_folder)
        os.makedirs(destination_folder, exist_ok=True)

        destination_file = destination_folder / item.name
        print(destination_file)
        shutil.move(str(item), str(destination_file))

        summary[category] += 1

        print(f"Moved {item.name} -> {category}/")

    return summary
  

def print_report(summary: dict) -> None: 
    if not summary:
        return
    print("-" * 20)
    print("Summary:")
    total = 0

    for category, count in summary.items():
        print(f"  {category}: {count} files")
        total += count

    print(f"\nTotal: {total} files organised.")

folder_path = r"C:\Users\Sandhya\Downloads"

summary = organise_folder(folder_path)
print_report(summary)