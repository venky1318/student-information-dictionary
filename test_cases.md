# Student Information Dictionary — Test Cases

## Testing Objective

To verify that the program correctly searches, adds, updates, and displays student records and handles invalid inputs.

## Test Cases

| Test ID | Test Scenario | Expected Result |
|---|---|---|
| TC01 | Search for S101 | Arun's record is displayed |
| TC02 | Search for an unknown ID | A not-found message appears |
| TC03 | Add a new student with ID S104 | Record is added successfully |
| TC04 | Add an existing ID such as S101 | Duplicate ID is rejected |
| TC05 | Update S102 | Existing student information is updated |
| TC06 | Update an unknown ID | A not-found message appears |
| TC07 | Enter an age of 0 or a negative age | Age is rejected |
| TC08 | Enter marks below 0 or above 100 | Marks are rejected |
| TC09 | Display all students | All stored records are displayed |
| TC10 | Enter an invalid menu choice | An error message appears |
| TC11 | Leave the name or course blank when adding | The record is rejected |
| TC12 | Exit using option 5 | The program terminates |

## Test Execution Record

Run each test in the program and record the actual result.

| Test ID | Actual Result | Status |
|---|---|---|
| TC01–TC12 | Record after execution | Pending |

## Testing Notes

Student additions and updates are stored in memory during the current program session. Restarting the program restores the original sample dataset.

Only mark a test as passed after verifying its actual output.

## Testing Conclusion

The test cases verify the main dictionary operations and help identify errors in record management and input validation.
