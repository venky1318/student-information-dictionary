# Student Information Dictionary


## Project Overview

Student Information Dictionary is a menu-driven Python program that stores and manages student records using a dictionary.

The program supports searching for students, adding new records, updating existing information, and displaying all stored records.

## Objective

To practise Python dictionaries and structured data representation while implementing basic student record management operations.

## Features

- Search students using unique student IDs.
- Add new student records.
- Update existing student information.
- Display all student records.
- Prevent duplicate student IDs.
- Validate age and marks.
- Handle invalid menu choices.

## Technologies Used

- Python 3
- Visual Studio Code
- GitHub

## Data Structure

Student IDs are used as dictionary keys. Each key maps to a nested dictionary containing the student's name, age, course, and marks.

Example:

`S101: {"name": "Arun", "age": 20, "course": "Python", "marks": 85}`

The sample records are fictional.

## How to Run

1. Install Python 3.
2. Clone or download this repository.
3. Open the folder in VS Code.
4. Open the terminal.
5. Run:

`python student_information.py`

On Windows, you can also try:

`py student_information.py`

## Menu Options

1. Search student
2. Add student
3. Update student
4. Display all students
5. Exit

## Validation

The program checks that student IDs are unique, names and courses are not empty, age is a positive integer, and marks fall between 0 and 100.

## Concepts Learned

- Python dictionaries
- Nested dictionaries
- Key-value pairs
- Functions
- Loops and conditional statements
- Input validation
- Exception handling
- Structured data management

## Limitations and Future Improvements

Records are stored in memory and are not saved after the program exits.

Future improvements could include saving records to JSON or CSV, adding record deletion, and building a graphical user interface.

## Conclusion

This project demonstrates how Python dictionaries can be used to organize and manage structured student information through simple operations.
