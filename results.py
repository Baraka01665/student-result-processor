PASS_MARK = 40


def calculate_result(student):
    marks = student["marks"]
    total = sum(marks.values())
    average = total / len(marks) if marks else 0
    passed = all(mark >= PASS_MARK for mark in marks.values())

    if not passed:
        grade = "F"
    elif average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "E"

    return {
        "total": total,
        "average": average,
        "grade": grade,
        "status": "PASS" if passed else "FAIL",
    }


def print_report(students):
    print("STUDENT RESULT REPORT")
    print("=" * 72)

    for student in students:
        result = calculate_result(student)
        marks_text = ", ".join(
            "{}: {}".format(subject, mark)
            for subject, mark in student["marks"].items()
        )
        print("Name: {} (ID: {})".format(student["name"], student["id"]))
        print("Marks: {}".format(marks_text))
        print(
            "Total: {} | Average: {:.2f} | Grade: {} | Status: {}".format(
                result["total"], result["average"],
                result["grade"], result["status"]
            )
        )
        print("-" * 72)
