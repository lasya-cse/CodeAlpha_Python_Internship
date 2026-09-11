# Task 3 - Task Automation with Python
## 📌 Project Overview
The JPG File Organizer is a Python-based automation script developed as part of the CodeAlpha Python Programming Internship. The program automatically identifies JPG and JPEG image files from a selected folder and moves them into a separate folder.
## 🎯 Objective
The objective of this project is to automate a common file management task using Python. It demonstrates how Python can be used to work with folders, identify files, create directories, and move files automatically.
## ✨ Features
- Automatically detects JPG and JPEG files
- Accepts a user-specified folder path
- Validates the folder path
- Creates a separate `JPG_Files` folder automatically
- Moves image files using Python
- Handles duplicate file names
- Displays files before organizing
- Asks for user confirmation
- Displays an organization summary
- Uses exception handling for file operations
## 🛠️ Technologies Used
- Python 3
- `os` Module
- `shutil` Module
- File Handling
- Functions
- Loops
- Conditional Statements
- Exception Handling
## ⚙️ How It Works
1. The user enters the path of the folder to organize.
2. The program checks whether the folder exists.
3. The program searches the folder for JPG and JPEG files.
4. The detected image files are displayed to the user.
5. The user confirms whether the files should be organized.
6. A `JPG_Files` folder is created if it does not already exist.
7. The image files are moved into the destination folder.
8. Duplicate file names are handled automatically.
9. The program displays the number of files moved and the destination folder.
## 📂 Project Structure
```text
Task3_Task_Automation/
├── file_organizer.py
└── README.md
