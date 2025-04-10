import os

project_structure = {
    ".": {
        "config": ["theme.py"],
        "data": ["flights.csv", "airports.csv"],
        "models": ["flight.py", "airport.py", "data_loader.py"],
        "widgets": ["__init__.py"],
        "actions": ["__init__.py"],
        "ui": ["__init__.py"],
        "": ["main.py"]
    }
}

def create_structure(base_path, structure):
    for folder, contents in structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        for subfolder, files in contents.items():
            subfolder_path = os.path.join(folder_path, subfolder)
            os.makedirs(subfolder_path, exist_ok=True)
            for file in files:
                file_path = os.path.join(subfolder_path, file)
                if not os.path.exists(file_path):
                    with open(file_path, "w", encoding="utf-8") as f:
                        if file.endswith(".py"):
                            f.write("# " + file.replace(".py", "").capitalize())
                        elif file.endswith(".csv"):
                            f.write("")  # fichier csv vide
                    print(f"✔️ Created: {file_path}")
                else:
                    print(f"⏭️ Skipped (already exists): {file_path}")

if __name__ == "__main__":
    create_structure(".", project_structure)
