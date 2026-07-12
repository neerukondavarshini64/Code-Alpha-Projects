import re

def analyze_code(code):
    issues = []

    lines = code.splitlines()

    for line_no, line in enumerate(lines, start=1):

        # SELECT *
        if "SELECT *" in line.upper():
            issues.append((
                "Low",
                line_no,
                "Use of SELECT *",
                "Specify only the required columns."
            ))

        # DROP TABLE
        if "DROP TABLE" in line.upper():
            issues.append((
                "High",
                line_no,
                "DROP TABLE Statement",
                "Avoid executing DROP TABLE in production."
            ))

        # DELETE without WHERE
        if "DELETE FROM" in line.upper() and "WHERE" not in line.upper():
            issues.append((
                "High",
                line_no,
                "DELETE Without WHERE",
                "Always use a WHERE clause with DELETE."
            ))

        # UPDATE without WHERE
        if "UPDATE" in line.upper() and "WHERE" not in line.upper():
            issues.append((
                "High",
                line_no,
                "UPDATE Without WHERE",
                "Always use a WHERE clause with UPDATE."
            ))

        # SQL Injection (string concatenation)
        if "SELECT" in line.upper() and "+" in line:
            issues.append((
                "High",
                line_no,
                "Possible SQL Injection",
                "Use parameterized queries or prepared statements."
            ))

        # TODO
        if "TODO" in line.upper():
            issues.append((
                "Low",
                line_no,
                "TODO Comment",
                "Review unfinished SQL before deployment."
            ))

    return issues