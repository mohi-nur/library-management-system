# Library Management System

A simple command-line Library Management System written in Python.  
The program allows users to add, view, update, delete, sort, and search for books while storing library data in both JSON and CSV files.

## Features

- Add new books with unique book IDs
- Validate book IDs using the `B001` format
- View all books and their availability status
- Update book title, author, and status
- Delete books with confirmation
- Search books by ID, title, or author
- Sort books by ID, title, or author
- Display library statistics
- Save data to both JSON and CSV files
- Load data from JSON first, with CSV as a fallback

## Technologies Used

- Python
- JSON
- CSV

This project uses only Python's built-in libraries, so no external packages are required.

## Project Structure

```text
Library-Management-System/
├── LibraryManagementSystem.py
├── book.json
├── book.csv
├── README.md
└── .gitignore
```

## How to Run

1. Make sure Python 3 is installed on your computer.
2. Download or clone this repository.
3. Keep `LibraryManagementSystem.py`, `book.json`, and `book.csv` in the same folder.
4. Open a terminal in the project folder.
5. Run:

```bash
python LibraryManagementSystem.py
```

On some systems, you may need to use:

```bash
python3 LibraryManagementSystem.py
```

## Menu Options

When the program starts, you can choose from:

```text
1. Add a book
2. View all
3. Update
4. Delete
5. Statistics
6. Sort
7. Search
8. Exit and save
```

## Data Storage

The program stores book information in two formats:

- `book.json` — the primary file used when loading saved books
- `book.csv` — a backup/fallback format

When you choose **Exit and save**, the current library data is written to both files.

Each book contains:

- Book ID
- Title
- Author
- Availability status

Example:

```text
B001 | To Kill A Mockingbird | Harper Lee | available
```

## Concepts Demonstrated

This project demonstrates:

- Object-oriented programming with Python classes
- Functions and program structure
- File handling
- JSON and CSV data storage
- Input validation
- Searching and sorting
- Error handling
- CRUD operations (Create, Read, Update, Delete)

## Possible Future Improvements

- Add a graphical user interface
- Track borrower names and return dates
- Add due-date reminders
- Use a database such as SQLite
- Add user accounts for librarians and members
- Add automated tests

## Author

Created by **mohi-nur**.
