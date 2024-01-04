import os
import subprocess

# Get the current script's directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# List of Python files to convert
python_files = [f"APP25.py"]

# Create a 'dist' folder if it doesn't exist
dist_folder = os.path.join(current_directory, "dist")
os.makedirs(dist_folder, exist_ok=True)

for python_file in python_files:
    # Generate the corresponding exe name by replacing ".py" with ".exe"
    exe_name = python_file.replace(".py", ".exe")

    # Run pyinstaller to convert the Python file to an executable
    print(f"Converting {python_file} to {exe_name}...")
    result = subprocess.run(["pyinstaller", "--onefile", "--noconsole", "--distpath", dist_folder, python_file], cwd=current_directory)

    if result.returncode != 0:
        print(f"Error converting {python_file}. Check the PyInstaller output for more details.")
        break

    print(f"Conversion successful for {python_file}.")

print("Conversion completed.")
