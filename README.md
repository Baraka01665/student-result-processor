# student-result-processor

A Python student result processor that calculates totals and averages, assigns grades, and reports each student’s pass/fail status based on their subject marks.

## Files

- `main.py` starts the report.
- `students.py` contains the student records and marks.
- `results.py` calculates each result and prints the report.

## Sample results

```text
STUDENT RESULT REPORT
========================================================================
Name: George (ID: S101)
Marks: IT: 92, Psychology: 85, Data science: 88
Total: 265 | Average: 88.33 | Grade: A | Status: PASS
------------------------------------------------------------------------
Name: Leah (ID: S102)
Marks: IT: 38, Psychology: 74, Data science: 65
Total: 177 | Average: 59.00 | Grade: F | Status: FAIL
------------------------------------------------------------------------
Name: Baraka (ID: S103)
Marks: IT: 76, Psychology: 81, Data science: 79
Total: 236 | Average: 78.67 | Grade: B | Status: PASS
------------------------------------------------------------------------
```
