# NPC & Monster XML Generator

## Description
A Python GUI tool to generate XML files for NPCs and Monsters in Open-Tibia servers. Built with Tkinter and optimized for Windows.

## Features
- User-friendly interface
- Generate NPC XML files
- Generate Monster XML files
- Open generated files directly
- Customizable output directory

## Installation

1. **Install Python 3.10+**

   - Go to the [Python official website](https://www.python.org/downloads/).
   - Download the latest Python 3.10+ installer for Windows.
   - Run the installer and make sure to check **"Add Python to PATH"** before clicking "Install Now".
   - After installation, verify Python is installed by opening Command Prompt and running:

     ```bash
     python --version
     ```
     It should display something like `Python 3.11.x`.

2. **Install required Python libraries**

   - Open Command Prompt in the project directory and run:
     ```bash
     pip install tk Pillow lxml
     ```

## Usage
To run the program directly with Python:
```bash
python main.py
```

## Compilation (Windows)
You can compile the project into a standalone executable using PyInstaller.

Open a terminal in the project directory and run:
```bash
python -m PyInstaller --onefile --windowed --name "NPC & Monster XML Generator" --add-data "favicon.ico;." main.py
```

- `--onefile`: bundles everything into a single executable.
- `--windowed`: runs without a console window.
- `--name`: sets the name of the generated .exe file.
- `--add-data`: includes additional files like icons.

After compilation, the executable will be located in the `dist` folder.
