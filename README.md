# 📁 Mini File System

A command-line based **file system simulator** developed using Python. This project is a practical implementation of fundamental concepts in **Computer Architecture and Organization**, particularly focusing on how file systems manage data, directories, and paths.

## ✨ Main Features

- **Directory Navigation:** `ls`, `cd`, `pwd`
- **File & Directory Manipulation:** `mkdir`, `touch`, `rm`, `cp`, `mv`
- **Content & Metadata Inspection:** `cat`, `stat`, `tree`, `find`
- **File Content Modification:** `write` (overwrite), `append` (add content), `replace` (replace text)
- **Data Persistence:** The file system state is automatically saved to `minifs.dat` when exiting and loaded when the application starts.

---

## 📂 Project Structure

```
MiniFileSystem/
├── src/
│   ├── cli.py          # Interface Layer: Handles user input and output.
│   ├── filesystem.py   # Logic Layer: Core implementation of file system operations.
│   ├── file_node.py    # Data Model Layer: Defines file and directory structures.
│   └── storage.py      # Persistence Layer: Handles saving and loading system states.
├── tests/
│   └── test_*.py       # Quality Assurance Layer: Automated tests for each component.
├── main.py             # Application entry point.
├── requirements.txt    # Project dependencies.
└── README.md           # Project documentation.
```

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```bash
git clone <your_repository_url>
cd MiniFileSystem
```

### 2. Create and Activate Virtual Environment

Create a virtual environment:

```bash
python -m venv venv
```

Activate on Windows:

```bash
.\venv\Scripts\activate
```

Activate on macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Use

### 1. Run the Application

```bash
python main.py
```

The application will start with the prompt:

```text
minifs:/$
```

### 2. Interaction

Use the available commands to interact with the simulated file system.

### 3. Exit

Type:

```bash
exit
```

or press:

```text
Ctrl + C
```

The current file system state will automatically be saved into `minifs.dat`. When the application is launched again, all previously created files and directories will be restored.

---

# 📖 Command Reference

## Navigation & Inspection

| Command | Example Usage | Description |
|---|---|---|
| `ls [path]` | `ls`, `ls /polman` | Displays the contents of a directory. Directories are marked with `/`. |
| `cd <path>` | `cd polman`, `cd ../` | Changes the current directory. |
| `pwd` | `pwd` | Displays the current directory path. |
| `find <name>` | `find profile.txt` | Searches for files or directories across the file system. |
| `stat <path>` | `stat /polman/profile.txt` | Displays detailed file/directory metadata information. |
| `tree [path]` | `tree`, `tree /polman` | Displays the directory structure in a tree format. |

---

## File & Directory Manipulation

| Command | Example Usage | Description |
|---|---|---|
| `mkdir <dir>` | `mkdir assignment` | Creates a new directory. |
| `touch <file>` | `touch notes.txt` | Creates a new empty file. |
| `cat <file>` | `cat notes.txt` | Displays file content. |
| `write <file> "..."` | `write file.txt "Hello World"` | Overwrites the entire file content. |
| `append <file> "..."` | `append file.txt " New Line"` | Adds content to the end of an existing file. |
| `replace <file> "A" "B"` | `replace file.txt "Hello" "Hi"` | Replaces all occurrences of text "A" with "B". |
| `rm <path>` | `rm notes.txt` | Removes an empty file or directory. |
| `cp <src> <dest>` | `cp file.txt /assignment/` | Copies a file to another location. |
| `mv <src> <dest>` | `mv file.txt new_file.txt` | Moves or renames a file. |

---

## Utilities

| Command | Description |
|---|---|
| `save` | Manually saves the current file system state. |
| `load` | Manually loads the file system state from `minifs.dat`. |
| `clear` | Clears the console screen. |
| `help` | Displays all available commands. |
| `exit` | Exits the application and saves the current state. |

---

## 🧪 Testing

This project includes unit tests to ensure every component works correctly.

Run all tests:

```bash
pytest
```

Run tests with coverage report:

```bash
pytest --cov=src
```

---

## 👥 Contributors

- Azfa Hafshiam Dilaga (2224443002)
- Bintang Shobri Al Chakim (224443003)
- Lukita Falencia Marjan (224443009)
- Muhammad Basit Rozak Akbar S.P (224443012)
- Muhammad Daffi Izzuddin (224443013)
- Raden Aryo Dwiputra Permana (224443017)
