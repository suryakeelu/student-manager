# Student Manager System

A lightweight command-line Student Management System built using Python. This application allows users to manage student records dynamically through an interactive menu.

---

## Features

- **Add Student**: Register a student with a unique integer ID, non-empty name, and marks between 0 and 100.
- **Display Students**: View a list of all registered students with their ID, name, and marks.
- **Search Student**: Find and view student details using their unique Student ID.
- **Update Marks**: Modify the marks of an existing student by ID with validation (0 to 100).
- **Delete Student**: Remove a student record from the system using their Student ID.
- **Find Topper**: Identify and display the student with the highest marks.
- **Input Validation**: Prevents duplicate IDs, empty names, out-of-range marks, and invalid menu choices.

---

## Technologies Used

- **Python 3**: Core language used for implementation.
- **Python Standard Library**: No external third-party packages or dependencies required.

---

## Requirements

- **Python 3.10 or newer**: Required because the codebase utilizes Python's structural pattern matching (`match-case` statements).

---

## How to Run

1. Clone or download this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/student-manager.git
   cd student-manager
   ```

2. Run the application using Python 3.10+:
   ```bash
   python project-StudentManagerSystem.py
   ```

---

## How to Use

When you run the script, an interactive menu will appear in your console:

```text
Student Menu
1. Add Student
2. Display Students
3. Search Student
4. Update Marks
5. Delete Student
6. Find Topper
7. Exit
```

1. Enter a number between `1` and `7` to choose an action.
2. Follow the on-screen prompts to input Student ID, Name, or Marks.
3. Select Option `7` to exit the application.

---

## Current Limitations

- **In-Memory Data Storage**: All student records are stored in memory (`self.students` list) during runtime. **Data is lost when the program exits.**
- **Single Topper Display**: If multiple students share the exact same top score, only the first student encountered is displayed.
- **Command-Line Interface**: Interactivity is limited to console text inputs and outputs.

---

## Future Improvements

- Implement persistent data storage (JSON, CSV, or SQLite) so student records persist across sessions.
- Enhance the `find_topper` feature to handle and display all tied top scorers.
- Add support for bulk student data import/export.
- Build a graphical user interface (GUI) or web interface.
