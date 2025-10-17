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
1. Make sure Python 3.10+ is installed.
2. Install required packages:
```bash
pip install -r requirements.txt
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
python -m PyInstaller --onefile --windowed --name "NPC_Monster_XML_Generator" --add-data "favicon.ico;." main.py
```

- `--onefile`: bundles everything into a single executable.
- `--windowed`: runs without a console window.
- `--name`: sets the name of the generated .exe file.
- `--add-data`: includes additional files like icons.

After compilation, the executable will be located in the `dist` folder.
